from dotenv import load_dotenv
import requests
import os

load_dotenv()

MOODLE_URL = "http://localhost/webservice/rest/server.php"
MOODLE_TOKEN = os.getenv("MOODLE_TOKEN")

MOODLE_ROLE_IDS = {
    "manager": 1,
    "teacher": 3,
    "coursecreator": 2,
}

SYSTEM_CONTEXT_ID = 1


def _call_moodle_api(wsfunction, payload):
    data = {
        "wstoken": MOODLE_TOKEN,
        "wsfunction": wsfunction,
        "moodlewsrestformat": "json",
        **payload,
    }
    response = requests.post(MOODLE_URL, headers=HEADERS, data=data)
    response.raise_for_status()
    result = response.json()

    if isinstance(result, dict) and "exception" in result:
        raise Exception(f"❌ Moodle API error: {result['message']}")

    return result


def delete_user(user_id):
    return _call_moodle_api(
        "core_user_delete_users",
        {
            "userids[0]": user_id,
        },
    )


def create_moodle_user(user, password):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # Step 1: Create Moodle user
    data = {
        "wstoken": MOODLE_TOKEN,
        "wsfunction": "core_user_create_users",
        "moodlewsrestformat": "json",
        "users[0][username]": user.username,
        "users[0][password]": password,
        "users[0][firstname]": user.first_name,
        "users[0][lastname]": user.last_name,
        "users[0][email]": user.email,
        "users[0][city]": user.city or "",
        "users[0][country]": user.country or "US",
    }

    response = requests.post(MOODLE_URL, headers=headers, data=data)
    response.raise_for_status()
    moodle_response = response.json()

    if "exception" in moodle_response:
        raise Exception(f"Moodle API error: {moodle_response['message']}")

    moodle_user_id = moodle_response[0]["id"]
    print(f"✅ Moodle user created with ID: {moodle_user_id}")

    # Step 2: Assign system-wide role for non-students
    if user.role == "teacher":
        role_id = MOODLE_ROLE_IDS["coursecreator"]
        print("#" * 200)
        print(f"Assigning course creator role ID {role_id} to user ID {moodle_user_id}")
        print("#" * 200)
        assign_system_role(moodle_user_id, role_id)

    elif user.role == "manager":
        role_id = MOODLE_ROLE_IDS[user.role]
        assign_system_role(moodle_user_id, role_id)

    return moodle_user_id


def assign_system_role(moodle_user_id, role_id):
    data = {
        "wstoken": MOODLE_TOKEN,
        "wsfunction": "core_role_assign_roles",
        "moodlewsrestformat": "json",
        "assignments[0][roleid]": role_id,
        "assignments[0][userid]": moodle_user_id,
        "assignments[0][contextid]": SYSTEM_CONTEXT_ID,
    }

    response = requests.post(MOODLE_URL, data=data)
    response.raise_for_status()

    print("Raw response text:", response.text)

    try:
        result = response.json() if response.text else {}
    except Exception as e:
        print(f"JSON parsing failed: {e}")
        raise

    if result is None:
        result = {}

    if "exception" in result:
        raise Exception(f"Failed to assign Moodle role: {result['message']}")

    print(
        f"✅ Assigned role ID {role_id} to user ID {moodle_user_id} at system context"
    )


def get_moodle_login_url(user):
    service = "moodle_mobile_app"  # default service that allows token login
    login_url = (
        f"{MOODLE_URL.replace('/webservice/rest/server.php', '')}/login/token.php"
    )
    payload = {
        "username": user.username,
        "password": user.raw_password,  # Save this temporarily during registration or store encrypted
        "service": service,
    }

    response = requests.post(login_url, data=payload)
    response.raise_for_status()
    data = response.json()

    if "error" in data:
        raise Exception(f"SSO Login Error: {data['error']}")

    token = data["token"]

    # Moodle autologin URL using token (redirects to dashboard or specific page)
    redirect_url = (
        f"{MOODLE_URL.replace('/webservice/rest/server.php', '')}/?wstoken={token}"
    )
    return redirect_url
