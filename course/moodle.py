from dotenv import load_dotenv
import requests
import os

load_dotenv()

MOODLE_URL = "http://localhost/webservice/rest/server.php"
MOODLE_TOKEN = os.getenv("MOODLE_TOKEN")
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


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


# ------------------------------
# 🎓 Course Operations
# ------------------------------


def delete_course(course_id):
    return _call_moodle_api(
        "core_course_delete_courses",
        {
            "courseids[0]": course_id,
        },
    )


def get_all_courses():
    return _call_moodle_api("core_course_get_courses", {})


def get_course_by_field(field, value):
    return _call_moodle_api(
        "core_course_get_courses_by_field",
        {
            "field": field,
            "value": value,
        },
    )


# ------------------------------
# 👤 User Operations
# ------------------------------


def get_user_by_field(field, value):
    return _call_moodle_api(
        "core_user_get_users_by_field",
        {
            "field": field,
            "values[0]": value,
        },
    )


# ------------------------------
# 📚 Enrollment Operations
# ------------------------------


def enroll_user(course_id, user_id, role_id=5):  # 5 = student
    return _call_moodle_api(
        "enrol_manual_enrol_users",
        {
            "enrolments[0][roleid]": role_id,
            "enrolments[0][userid]": user_id,
            "enrolments[0][courseid]": course_id,
        },
    )


def unenroll_user(course_id, user_id, role_id=5):
    return _call_moodle_api(
        "enrol_manual_unenrol_users",
        {
            "enrolments[0][roleid]": role_id,
            "enrolments[0][userid]": user_id,
            "enrolments[0][courseid]": course_id,
        },
    )


def get_enrolled_users(course_id):
    return _call_moodle_api(
        "core_enrol_get_enrolled_users",
        {
            "courseid": course_id,
        },
    )


def get_user_courses(user_id):
    return _call_moodle_api(
        "core_enrol_get_users_courses",
        {
            "userid": user_id,
        },
    )


# ------------------------------
# 🧑‍🏫 Role Management
# ------------------------------


def assign_system_role(user_id, role_id, context_id=1):  # 1 = system
    return _call_moodle_api(
        "core_role_assign_roles",
        {
            "assignments[0][roleid]": role_id,
            "assignments[0][userid]": user_id,
            "assignments[0][contextid]": context_id,
        },
    )


def unassign_system_role(user_id, role_id, context_id=1):
    return _call_moodle_api(
        "core_role_unassign_roles",
        {
            "unassignments[0][roleid]": role_id,
            "unassignments[0][userid]": user_id,
            "unassignments[0][contextid]": context_id,
        },
    )


# ------------------------------
# 🧪 Utility / Support
# ------------------------------


def get_site_info():
    return _call_moodle_api("core_webservice_get_site_info", {})


def get_categories():
    return _call_moodle_api("core_course_get_categories", {})
