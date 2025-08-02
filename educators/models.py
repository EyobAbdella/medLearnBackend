# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activations(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    code = models.CharField(max_length=120)
    completed = models.IntegerField()
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "activations"


class AdminNotifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    action_label = models.CharField(max_length=191, blank=True, null=True)
    action_url = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    permission = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "admin_notifications"


class Ads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    expired_at = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    key = models.CharField(unique=True, max_length=120)
    image = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    clicked = models.BigIntegerField()
    order = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    open_in_new_tab = models.IntegerField()
    tablet_image = models.CharField(max_length=191, blank=True, null=True)
    mobile_image = models.CharField(max_length=191, blank=True, null=True)
    ads_type = models.CharField(max_length=191, blank=True, null=True)
    google_adsense_slot_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ads"


class AdsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ads_id")
    lang_code = models.CharField(max_length=191)
    ads_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    tablet_image = models.CharField(max_length=191, blank=True, null=True)
    mobile_image = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ads_translations"


class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    content = models.TextField()
    has_action = models.IntegerField()
    action_label = models.CharField(max_length=60, blank=True, null=True)
    action_url = models.CharField(max_length=400, blank=True, null=True)
    action_open_new_tab = models.IntegerField()
    dismissible = models.IntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "announcements"


class AnnouncementsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "announcements_id")
    lang_code = models.CharField(max_length=191)
    announcements_id = models.PositiveBigIntegerField()
    content = models.TextField(blank=True, null=True)
    action_label = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "announcements_translations"


class AuditHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    user_type = models.CharField(max_length=191, blank=True, null=True)
    module = models.CharField(max_length=60)
    request = models.TextField(blank=True, null=True)
    action = models.CharField(max_length=120)
    user_agent = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    actor_id = models.PositiveBigIntegerField()
    actor_type = models.CharField(max_length=191, blank=True, null=True)
    reference_id = models.PositiveBigIntegerField()
    reference_name = models.CharField(max_length=191)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "audit_histories"


class Cache(models.Model):
    key = models.CharField(primary_key=True, max_length=191)
    value = models.TextField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cache"


class CacheLocks(models.Model):
    key = models.CharField(primary_key=True, max_length=191)
    owner = models.CharField(max_length=191)
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cache_locks"


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    parent_id = models.PositiveBigIntegerField()
    description = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=60)
    author_id = models.PositiveBigIntegerField(blank=True, null=True)
    author_type = models.CharField(max_length=191)
    icon = models.CharField(max_length=60, blank=True, null=True)
    order = models.PositiveIntegerField()
    is_featured = models.IntegerField()
    is_default = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "categories"


class CategoriesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "categories_id")
    lang_code = models.CharField(max_length=20)
    categories_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "categories_translations"


class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.CharField(unique=True, max_length=120, blank=True, null=True)
    state_id = models.PositiveBigIntegerField(blank=True, null=True)
    country_id = models.PositiveBigIntegerField(blank=True, null=True)
    record_id = models.CharField(max_length=40, blank=True, null=True)
    order = models.IntegerField()
    image = models.CharField(max_length=191, blank=True, null=True)
    is_default = models.PositiveIntegerField()
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cities"


class CitiesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "cities_id")
    lang_code = models.CharField(max_length=20)
    cities_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cities_translations"


class ContactCustomFieldOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    custom_field_id = models.PositiveBigIntegerField()
    label = models.CharField(max_length=191, blank=True, null=True)
    value = models.CharField(max_length=191)
    order = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "contact_custom_field_options"


class ContactCustomFieldOptionsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "contact_custom_field_options_id")
    contact_custom_field_options_id = models.PositiveBigIntegerField()
    lang_code = models.CharField(max_length=191)
    label = models.CharField(max_length=191, blank=True, null=True)
    value = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "contact_custom_field_options_translations"


class ContactCustomFields(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=191)
    required = models.IntegerField()
    name = models.CharField(max_length=191)
    placeholder = models.CharField(max_length=191, blank=True, null=True)
    order = models.IntegerField()
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "contact_custom_fields"


class ContactCustomFieldsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "contact_custom_fields_id")
    contact_custom_fields_id = models.PositiveBigIntegerField()
    lang_code = models.CharField(max_length=191)
    name = models.CharField(max_length=191, blank=True, null=True)
    placeholder = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "contact_custom_fields_translations"


class ContactReplies(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    contact_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "contact_replies"


class Contacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True, null=True)
    content = models.TextField()
    custom_fields = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "contacts"


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=120, blank=True, null=True)
    order = models.IntegerField()
    image = models.CharField(max_length=191, blank=True, null=True)
    is_default = models.PositiveIntegerField()
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "countries"


class CountriesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "countries_id")
    lang_code = models.CharField(max_length=20)
    countries_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=120, blank=True, null=True)
    nationality = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "countries_translations"


class DashboardWidgetSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    settings = models.TextField(blank=True, null=True)
    user_id = models.PositiveBigIntegerField()
    widget_id = models.PositiveBigIntegerField()
    order = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dashboard_widget_settings"


class DashboardWidgets(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dashboard_widgets"


class DeviceTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=191)
    platform = models.CharField(max_length=191, blank=True, null=True)
    app_version = models.CharField(max_length=191, blank=True, null=True)
    device_id = models.CharField(max_length=191, blank=True, null=True)
    user_type = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "device_tokens"


class EcBrands(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    logo = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=60)
    order = models.PositiveIntegerField()
    is_featured = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_brands"


class EcBrandsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_brands_id")
    lang_code = models.CharField(max_length=191)
    ec_brands_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_brands_translations"


class EcCart(models.Model):
    pk = models.CompositePrimaryKey("identifier", "instance")
    identifier = models.CharField(max_length=60)
    instance = models.CharField(max_length=60)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_cart"


class EcCurrencies(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    symbol = models.CharField(max_length=10)
    is_prefix_symbol = models.PositiveIntegerField()
    decimals = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    is_default = models.IntegerField()
    exchange_rate = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_currencies"


class EcCustomerAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField()
    is_default = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_customer_addresses"


class EcCustomerPasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_customer_password_resets"


class EcCustomerRecentlyViewedProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_customer_recently_viewed_products"


class EcCustomerUsedCoupons(models.Model):
    pk = models.CompositePrimaryKey("discount_id", "customer_id")
    discount_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_customer_used_coupons"


class EcCustomers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191)
    avatar = models.CharField(max_length=191, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    email_verify_token = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=60)
    block_reason = models.CharField(max_length=400, blank=True, null=True)
    private_notes = models.TextField(blank=True, null=True)
    stripe_account_id = models.CharField(max_length=191, blank=True, null=True)
    stripe_account_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = "ec_customers"


class EcDiscountCustomers(models.Model):
    pk = models.CompositePrimaryKey("discount_id", "customer_id")
    discount_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_discount_customers"


class EcDiscountProductCategories(models.Model):
    pk = models.CompositePrimaryKey("discount_id", "product_category_id")
    discount_id = models.PositiveBigIntegerField()
    product_category_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_discount_product_categories"


class EcDiscountProductCollections(models.Model):
    pk = models.CompositePrimaryKey("discount_id", "product_collection_id")
    discount_id = models.PositiveBigIntegerField()
    product_collection_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_discount_product_collections"


class EcDiscountProducts(models.Model):
    pk = models.CompositePrimaryKey("discount_id", "product_id")
    discount_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_discount_products"


class EcDiscounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total_used = models.PositiveIntegerField()
    value = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=60, blank=True, null=True)
    can_use_with_promotion = models.IntegerField()
    can_use_with_flash_sale = models.IntegerField()
    discount_on = models.CharField(max_length=20, blank=True, null=True)
    product_quantity = models.PositiveIntegerField(blank=True, null=True)
    type_option = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    min_order_price = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    apply_via_url = models.IntegerField()
    display_at_checkout = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    store_id = models.PositiveBigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_discounts"


class EcFlashSaleProducts(models.Model):
    flash_sale_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()
    price = models.FloatField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    sold = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "ec_flash_sale_products"


class EcFlashSales(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_flash_sales"


class EcFlashSalesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_flash_sales_id")
    lang_code = models.CharField(max_length=191)
    ec_flash_sales_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_flash_sales_translations"


class EcGlobalOptionValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    option_id = models.PositiveBigIntegerField(db_comment="option id")
    option_value = models.TextField(blank=True, null=True, db_comment="option value")
    affect_price = models.FloatField(
        blank=True, null=True, db_comment="value of price of this option affect"
    )
    order = models.IntegerField()
    affect_type = models.IntegerField(db_comment="0. fixed 1. percent")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_global_option_value"


class EcGlobalOptionValueTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_global_option_value_id")
    lang_code = models.CharField(max_length=191)
    ec_global_option_value_id = models.PositiveBigIntegerField()
    option_value = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_global_option_value_translations"


class EcGlobalOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191, db_comment="Name of options")
    option_type = models.CharField(max_length=191, db_comment="option type")
    required = models.IntegerField(db_comment="Checked if this option is required")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_global_options"


class EcGlobalOptionsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_global_options_id")
    lang_code = models.CharField(max_length=191)
    ec_global_options_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_global_options_translations"


class EcGroupedProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_product_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()
    fixed_qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = "ec_grouped_products"


class EcInvoiceItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_id = models.PositiveBigIntegerField()
    reference_type = models.CharField(max_length=191)
    reference_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=400, blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sub_total = models.DecimalField(max_digits=15, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=15, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    options = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_invoice_items"


class EcInvoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference_type = models.CharField(max_length=191)
    reference_id = models.PositiveBigIntegerField()
    code = models.CharField(unique=True, max_length=191)
    customer_name = models.CharField(max_length=191, blank=True, null=True)
    company_name = models.CharField(max_length=191, blank=True, null=True)
    company_logo = models.CharField(max_length=191, blank=True, null=True)
    customer_email = models.CharField(max_length=191, blank=True, null=True)
    customer_phone = models.CharField(max_length=191, blank=True, null=True)
    customer_address = models.CharField(max_length=191, blank=True, null=True)
    customer_tax_id = models.CharField(max_length=191, blank=True, null=True)
    sub_total = models.DecimalField(max_digits=15, decimal_places=2)
    tax_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    shipping_amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_fee = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    discount_amount = models.DecimalField(max_digits=15, decimal_places=2)
    shipping_option = models.CharField(max_length=60, blank=True, null=True)
    shipping_method = models.CharField(max_length=60)
    coupon_code = models.CharField(max_length=120, blank=True, null=True)
    discount_description = models.CharField(max_length=191, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    payment_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=191)
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_invoices"


class EcOptionValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    option_id = models.PositiveBigIntegerField(db_comment="option id")
    option_value = models.TextField(blank=True, null=True, db_comment="option value")
    affect_price = models.FloatField(
        blank=True, null=True, db_comment="value of price of this option affect"
    )
    order = models.IntegerField()
    affect_type = models.IntegerField(db_comment="0. fixed 1. percent")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_option_value"


class EcOptionValueTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_option_value_id")
    lang_code = models.CharField(max_length=191)
    ec_option_value_id = models.PositiveBigIntegerField()
    option_value = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_option_value_translations"


class EcOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191, db_comment="Name of options")
    option_type = models.CharField(
        max_length=191, blank=True, null=True, db_comment="option type"
    )
    product_id = models.PositiveBigIntegerField()
    order = models.IntegerField()
    required = models.IntegerField(db_comment="Checked if this option is required")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_options"


class EcOptionsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_options_id")
    lang_code = models.CharField(max_length=191)
    ec_options_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_options_translations"


class EcOrderAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    order_id = models.PositiveBigIntegerField()
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = "ec_order_addresses"


class EcOrderHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=120)
    description = models.CharField(max_length=400, blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField()
    extras = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_order_histories"


class EcOrderProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    tax_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    options = models.TextField(blank=True, null=True)
    product_options = models.TextField(
        blank=True, null=True, db_comment="product option data"
    )
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=191)
    product_image = models.CharField(max_length=191, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    restock_quantity = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    product_type = models.CharField(max_length=60)
    times_downloaded = models.IntegerField()
    license_code = models.CharField(max_length=36, blank=True, null=True)
    downloaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_order_product"


class EcOrderReferrals(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.CharField(max_length=39, blank=True, null=True)
    landing_domain = models.CharField(max_length=191, blank=True, null=True)
    landing_page = models.CharField(max_length=191, blank=True, null=True)
    landing_params = models.CharField(max_length=191, blank=True, null=True)
    referral = models.CharField(max_length=191, blank=True, null=True)
    gclid = models.CharField(max_length=191, blank=True, null=True)
    fclid = models.CharField(max_length=191, blank=True, null=True)
    utm_source = models.CharField(max_length=191, blank=True, null=True)
    utm_campaign = models.CharField(max_length=191, blank=True, null=True)
    utm_medium = models.CharField(max_length=191, blank=True, null=True)
    utm_term = models.CharField(max_length=191, blank=True, null=True)
    utm_content = models.CharField(max_length=191, blank=True, null=True)
    referrer_url = models.TextField(blank=True, null=True)
    referrer_domain = models.CharField(max_length=191, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_order_referrals"


class EcOrderReturnHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_return_id = models.PositiveBigIntegerField()
    action = models.CharField(max_length=191)
    description = models.CharField(max_length=400, blank=True, null=True)
    reason = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_order_return_histories"


class EcOrderReturnItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_return_id = models.PositiveBigIntegerField(db_comment="Order return id")
    order_product_id = models.PositiveBigIntegerField(db_comment="Order product id")
    product_id = models.PositiveBigIntegerField(db_comment="Product id")
    product_name = models.CharField(max_length=191)
    product_image = models.CharField(max_length=191, blank=True, null=True)
    qty = models.IntegerField(db_comment="Quantity return")
    price = models.DecimalField(
        max_digits=15, decimal_places=2, db_comment="Price Product"
    )
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    refund_amount = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ec_order_return_items"


class EcOrderReturns(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=191, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(db_comment="Order ID")
    store_id = models.PositiveBigIntegerField(
        blank=True, null=True, db_comment="Store ID"
    )
    user_id = models.PositiveBigIntegerField(db_comment="Customer ID")
    reason = models.TextField(blank=True, null=True, db_comment="Reason return order")
    order_status = models.CharField(
        max_length=191, blank=True, null=True, db_comment="Order current status"
    )
    return_status = models.CharField(max_length=191, db_comment="Return status")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_order_returns"


class EcOrderTaxInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    company_name = models.CharField(max_length=120)
    company_address = models.CharField(max_length=191)
    company_tax_code = models.CharField(max_length=20)
    company_email = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_order_tax_information"


class EcOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=191, blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    shipping_option = models.CharField(max_length=60, blank=True, null=True)
    shipping_method = models.CharField(max_length=60)
    status = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    tax_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    shipping_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    payment_fee = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)
    coupon_code = models.CharField(max_length=120, blank=True, null=True)
    discount_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    sub_total = models.DecimalField(max_digits=15, decimal_places=2)
    is_confirmed = models.IntegerField()
    discount_description = models.CharField(max_length=191, blank=True, null=True)
    is_finished = models.IntegerField(blank=True, null=True)
    cancellation_reason = models.CharField(max_length=191, blank=True, null=True)
    cancellation_reason_description = models.CharField(
        max_length=191, blank=True, null=True
    )
    completed_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=120, blank=True, null=True)
    payment_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    proof_file = models.CharField(max_length=191, blank=True, null=True)
    private_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_orders"


class EcProductAttributeSets(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, blank=True, null=True)
    display_layout = models.CharField(max_length=191)
    is_searchable = models.PositiveIntegerField()
    is_comparable = models.PositiveIntegerField()
    is_use_in_product_listing = models.PositiveIntegerField()
    status = models.CharField(max_length=60)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    use_image_from_product_variation = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_attribute_sets"


class EcProductAttributeSetsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_product_attribute_sets_id")
    lang_code = models.CharField(max_length=191)
    ec_product_attribute_sets_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_attribute_sets_translations"


class EcProductAttributes(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute_set_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, blank=True, null=True)
    color = models.CharField(max_length=120, blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    is_default = models.PositiveIntegerField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_attributes"


class EcProductAttributesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_product_attributes_id")
    lang_code = models.CharField(max_length=191)
    ec_product_attributes_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_attributes_translations"


class EcProductCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    parent_id = models.PositiveBigIntegerField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=60)
    order = models.PositiveIntegerField()
    image = models.CharField(max_length=191, blank=True, null=True)
    is_featured = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    icon = models.CharField(max_length=191, blank=True, null=True)
    icon_image = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_categories"


class EcProductCategoriesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_product_categories_id")
    lang_code = models.CharField(max_length=191)
    ec_product_categories_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_categories_translations"


class EcProductCategorizables(models.Model):
    pk = models.CompositePrimaryKey("category_id", "reference_id", "reference_type")
    category_id = models.PositiveBigIntegerField()
    reference_id = models.PositiveBigIntegerField()
    reference_type = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = "ec_product_categorizables"


class EcProductCategoryProduct(models.Model):
    pk = models.CompositePrimaryKey("product_id", "category_id")
    category_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_category_product"


class EcProductCollectionProducts(models.Model):
    pk = models.CompositePrimaryKey("product_id", "product_collection_id")
    product_collection_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_collection_products"


class EcProductCollections(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    slug = models.CharField(max_length=191)
    description = models.CharField(max_length=400, blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_featured = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_collections"


class EcProductCollectionsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_product_collections_id")
    lang_code = models.CharField(max_length=191)
    ec_product_collections_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_collections_translations"


class EcProductCrossSaleRelations(models.Model):
    pk = models.CompositePrimaryKey("from_product_id", "to_product_id")
    from_product_id = models.PositiveBigIntegerField()
    to_product_id = models.PositiveBigIntegerField()
    is_variant = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_type = models.CharField(max_length=191)
    apply_to_all_variations = models.IntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_cross_sale_relations"


class EcProductFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    url = models.CharField(max_length=400, blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_files"


class EcProductLabelProducts(models.Model):
    pk = models.CompositePrimaryKey("product_label_id", "product_id")
    product_label_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_label_products"


class EcProductLabels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    color = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    text_color = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_labels"


class EcProductLabelsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_product_labels_id")
    lang_code = models.CharField(max_length=191)
    ec_product_labels_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_labels_translations"


class EcProductLicenseCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField()
    license_code = models.CharField(unique=True, max_length=191)
    status = models.CharField(max_length=60)
    assigned_order_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    assigned_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_license_codes"


class EcProductRelatedRelations(models.Model):
    pk = models.CompositePrimaryKey("from_product_id", "to_product_id")
    from_product_id = models.PositiveBigIntegerField()
    to_product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_related_relations"


class EcProductSpecificationAttribute(models.Model):
    pk = models.CompositePrimaryKey("product_id", "attribute_id")
    product_id = models.PositiveBigIntegerField()
    attribute_id = models.PositiveBigIntegerField()
    value = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_specification_attribute"


class EcProductTagProduct(models.Model):
    pk = models.CompositePrimaryKey("product_id", "tag_id")
    product_id = models.PositiveBigIntegerField()
    tag_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_tag_product"


class EcProductTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_tags"


class EcProductTagsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_product_tags_id")
    lang_code = models.CharField(max_length=191)
    ec_product_tags_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_product_tags_translations"


class EcProductUpSaleRelations(models.Model):
    pk = models.CompositePrimaryKey("from_product_id", "to_product_id")
    from_product_id = models.PositiveBigIntegerField()
    to_product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_up_sale_relations"


class EcProductVariationItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute_id = models.PositiveBigIntegerField()
    variation_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_variation_items"
        unique_together = (("attribute_id", "variation_id"),)


class EcProductVariations(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    configurable_product_id = models.PositiveBigIntegerField()
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_variations"
        unique_together = (("product_id", "configurable_product_id"),)


class EcProductViews(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField()
    views = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = "ec_product_views"
        unique_together = (("product_id", "date"),)


class EcProductWithAttributeSet(models.Model):
    pk = models.CompositePrimaryKey("product_id", "attribute_set_id")
    attribute_set_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()
    order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "ec_product_with_attribute_set"


class EcProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=60)
    images = models.TextField(blank=True, null=True)
    video_media = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=191, blank=True, null=True)
    order = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(blank=True, null=True)
    allow_checkout_when_out_of_stock = models.PositiveIntegerField()
    with_storehouse_management = models.PositiveIntegerField()
    stock_status = models.CharField(max_length=191, blank=True, null=True)
    is_featured = models.PositiveIntegerField()
    brand_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_variation = models.IntegerField()
    sale_type = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    wide = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    tax_id = models.PositiveBigIntegerField(blank=True, null=True)
    views = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_by_type = models.CharField(max_length=191)
    image = models.CharField(max_length=191, blank=True, null=True)
    product_type = models.CharField(max_length=60, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    cost_per_item = models.FloatField(blank=True, null=True)
    generate_license_code = models.IntegerField()
    license_code_type = models.CharField(max_length=14)
    minimum_order_quantity = models.PositiveIntegerField(blank=True, null=True)
    maximum_order_quantity = models.PositiveIntegerField(blank=True, null=True)
    notify_attachment_updated = models.IntegerField()
    specification_table_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_products"


class EcProductsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_products_id")
    lang_code = models.CharField(max_length=191)
    ec_products_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_products_translations"


class EcReviewReplies(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    review_id = models.PositiveBigIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_review_replies"
        unique_together = (("review_id", "user_id"),)


class EcReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=191, blank=True, null=True)
    customer_email = models.CharField(max_length=191, blank=True, null=True)
    product_id = models.PositiveBigIntegerField()
    star = models.FloatField()
    comment = models.TextField()
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_reviews"
        unique_together = (("product_id", "customer_id"),)


class EcSharedWishlists(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=191)
    product_ids = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_shared_wishlists"


class EcShipmentHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=120)
    description = models.CharField(max_length=400, blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    shipment_id = models.PositiveBigIntegerField()
    order_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = "ec_shipment_histories"


class EcShipments(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    shipment_id = models.CharField(max_length=120, blank=True, null=True)
    rate_id = models.CharField(max_length=120, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=120)
    cod_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    cod_status = models.CharField(max_length=60)
    cross_checking_status = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    store_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tracking_id = models.CharField(max_length=191, blank=True, null=True)
    shipping_company_name = models.CharField(max_length=191, blank=True, null=True)
    tracking_link = models.CharField(max_length=191, blank=True, null=True)
    estimate_date_shipped = models.DateTimeField(blank=True, null=True)
    date_shipped = models.DateTimeField(blank=True, null=True)
    customer_delivered_confirmed_at = models.DateTimeField(blank=True, null=True)
    label_url = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_shipments"


class EcShipping(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_shipping"


class EcShippingRuleItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    shipping_rule_id = models.PositiveBigIntegerField()
    country = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    adjustment_price = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    is_enabled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_shipping_rule_items"


class EcShippingRules(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    shipping_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=24, blank=True, null=True)
    from_field = models.DecimalField(
        db_column="from", max_digits=15, decimal_places=2, blank=True, null=True
    )  # Field renamed because it was a Python reserved word.
    to = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_shipping_rules"


class EcSpecificationAttributes(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191)
    type = models.CharField(max_length=20)
    options = models.TextField(blank=True, null=True)
    default_value = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    author_type = models.CharField(max_length=191, blank=True, null=True)
    author_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_specification_attributes"


class EcSpecificationAttributesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_specification_attributes_id")
    lang_code = models.CharField(max_length=20)
    ec_specification_attributes_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    default_value = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_specification_attributes_translations"


class EcSpecificationGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    author_type = models.CharField(max_length=191, blank=True, null=True)
    author_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_specification_groups"


class EcSpecificationGroupsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_specification_groups_id")
    lang_code = models.CharField(max_length=20)
    ec_specification_groups_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_specification_groups_translations"


class EcSpecificationTableGroup(models.Model):
    pk = models.CompositePrimaryKey("table_id", "group_id")
    table_id = models.PositiveBigIntegerField()
    group_id = models.PositiveBigIntegerField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = "ec_specification_table_group"


class EcSpecificationTables(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=400, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    author_type = models.CharField(max_length=191, blank=True, null=True)
    author_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_specification_tables"


class EcSpecificationTablesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_specification_tables_id")
    lang_code = models.CharField(max_length=20)
    ec_specification_tables_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_specification_tables_translations"


class EcStoreLocators(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=191)
    country = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    is_primary = models.IntegerField(blank=True, null=True)
    is_shipping_location = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_store_locators"


class EcTaxProducts(models.Model):
    pk = models.CompositePrimaryKey("product_id", "tax_id")
    tax_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "ec_tax_products"


class EcTaxRules(models.Model):
    id = models.BigAutoField(primary_key=True)
    tax_id = models.PositiveBigIntegerField()
    country = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    is_enabled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_tax_rules"


class EcTaxes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191, blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_taxes"


class EcTaxesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "ec_taxes_id")
    lang_code = models.CharField(max_length=191)
    ec_taxes_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_taxes_translations"


class EcWishLists(models.Model):
    pk = models.CompositePrimaryKey("customer_id", "product_id")
    customer_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ec_wish_lists"


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=191)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "failed_jobs"


class FaqCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    order = models.IntegerField()
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "faq_categories"


class FaqCategoriesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "faq_categories_id")
    lang_code = models.CharField(max_length=20)
    faq_categories_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "faq_categories_translations"


class Faqs(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    category_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "faqs"


class FaqsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "faqs_id")
    lang_code = models.CharField(max_length=20)
    faqs_id = models.PositiveBigIntegerField()
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "faqs_translations"


class Galleries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    is_featured = models.PositiveIntegerField()
    order = models.PositiveIntegerField()
    image = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "galleries"


class GalleriesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "galleries_id")
    lang_code = models.CharField(max_length=20)
    galleries_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "galleries_translations"


class GalleryMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    images = models.TextField(blank=True, null=True)
    reference_id = models.PositiveBigIntegerField()
    reference_type = models.CharField(max_length=120)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gallery_meta"


class GalleryMetaTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "gallery_meta_id")
    lang_code = models.CharField(max_length=20)
    gallery_meta_id = models.PositiveBigIntegerField()
    images = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gallery_meta_translations"


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=191)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "jobs"


class LanguageMeta(models.Model):
    lang_meta_id = models.BigAutoField(primary_key=True)
    lang_meta_code = models.CharField(max_length=20, blank=True, null=True)
    lang_meta_origin = models.CharField(max_length=32)
    reference_id = models.PositiveBigIntegerField()
    reference_type = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = "language_meta"


class Languages(models.Model):
    lang_id = models.BigAutoField(primary_key=True)
    lang_name = models.CharField(max_length=120)
    lang_locale = models.CharField(max_length=20)
    lang_code = models.CharField(max_length=20)
    lang_flag = models.CharField(max_length=20, blank=True, null=True)
    lang_is_default = models.PositiveIntegerField()
    lang_order = models.IntegerField()
    lang_is_rtl = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = "languages"


class MbEnrollmentLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=191)
    course_code = models.CharField(max_length=191)
    api_response = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=9)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mb_enrollment_logs"


class MediaFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191)
    alt = models.CharField(max_length=191, blank=True, null=True)
    folder_id = models.PositiveBigIntegerField()
    mime_type = models.CharField(max_length=120)
    size = models.IntegerField()
    url = models.CharField(max_length=191)
    options = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    visibility = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = "media_files"


class MediaFolders(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    color = models.CharField(max_length=191, blank=True, null=True)
    slug = models.CharField(max_length=191, blank=True, null=True)
    parent_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "media_folders"


class MediaSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=120)
    value = models.TextField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "media_settings"


class MenuLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu_id = models.PositiveBigIntegerField()
    location = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "menu_locations"


class MenuNodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu_id = models.PositiveBigIntegerField()
    parent_id = models.PositiveBigIntegerField()
    reference_id = models.PositiveBigIntegerField(blank=True, null=True)
    reference_type = models.CharField(max_length=191, blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    icon_font = models.CharField(max_length=191, blank=True, null=True)
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=191, blank=True, null=True)
    css_class = models.CharField(max_length=191, blank=True, null=True)
    target = models.CharField(max_length=20)
    has_child = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "menu_nodes"


class Menus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.CharField(unique=True, max_length=120, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "menus"


class MetaBoxes(models.Model):
    id = models.BigAutoField(primary_key=True)
    meta_key = models.CharField(max_length=191)
    meta_value = models.TextField(blank=True, null=True)
    reference_id = models.PositiveBigIntegerField()
    reference_type = models.CharField(max_length=120)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "meta_boxes"


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = "migrations"


class MoodleBulkEnrollments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "moodle_bulk_enrollments"


class MoodleBulkEnrollmentsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "moodle_bulk_enrollments_id")
    lang_code = models.CharField(max_length=191)
    moodle_bulk_enrollments_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "moodle_bulk_enrollments_translations"


class Newsletters(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=120)
    name = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "newsletters"


class Pages(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    template = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pages"


class PagesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "pages_id")
    lang_code = models.CharField(max_length=20)
    pages_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pages_translations"


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "password_reset_tokens"


class PaymentLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_method = models.CharField(max_length=191)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=45)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "payment_logs"


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    currency = models.CharField(max_length=120, blank=True, null=True)
    user_id = models.PositiveBigIntegerField()
    charge_id = models.CharField(max_length=191, blank=True, null=True)
    payment_channel = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_fee = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=60, blank=True, null=True)
    payment_type = models.CharField(max_length=191, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    refunded_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    refund_note = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    customer_type = models.CharField(max_length=191, blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "payments"


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=191)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "personal_access_tokens"


class PostCategories(models.Model):
    category_id = models.PositiveBigIntegerField()
    post_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "post_categories"


class PostTags(models.Model):
    tag_id = models.PositiveBigIntegerField()
    post_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = "post_tags"


class Posts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    description = models.CharField(max_length=400, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=60)
    author_id = models.PositiveBigIntegerField(blank=True, null=True)
    author_type = models.CharField(max_length=191)
    is_featured = models.PositiveIntegerField()
    image = models.CharField(max_length=191, blank=True, null=True)
    views = models.PositiveIntegerField()
    format_type = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "posts"


class PostsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "posts_id")
    lang_code = models.CharField(max_length=20)
    posts_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "posts_translations"


class PushNotificationRecipients(models.Model):
    id = models.BigAutoField(primary_key=True)
    push_notification_id = models.PositiveBigIntegerField()
    user_type = models.CharField(max_length=191)
    user_id = models.PositiveBigIntegerField()
    device_token = models.CharField(max_length=191, blank=True, null=True)
    platform = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=191)
    sent_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    clicked_at = models.DateTimeField(blank=True, null=True)
    fcm_response = models.JSONField(blank=True, null=True)
    error_message = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "push_notification_recipients"


class PushNotifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    message = models.TextField()
    type = models.CharField(max_length=191)
    target_type = models.CharField(max_length=191, blank=True, null=True)
    target_value = models.CharField(max_length=191, blank=True, null=True)
    action_url = models.CharField(max_length=191, blank=True, null=True)
    image_url = models.CharField(max_length=191, blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=191)
    sent_count = models.IntegerField()
    failed_count = models.IntegerField()
    delivered_count = models.IntegerField()
    read_count = models.IntegerField()
    scheduled_at = models.DateTimeField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "push_notifications"


class RequestLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_code = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    count = models.PositiveIntegerField()
    user_id = models.CharField(max_length=191, blank=True, null=True)
    referrer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "request_logs"


class Revisions(models.Model):
    id = models.BigAutoField(primary_key=True)
    revisionable_type = models.CharField(max_length=191)
    revisionable_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    key = models.CharField(max_length=120)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "revisions"


class RoleUsers(models.Model):
    pk = models.CompositePrimaryKey("user_id", "role_id")
    user_id = models.PositiveBigIntegerField()
    role_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "role_users"


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(unique=True, max_length=120)
    name = models.CharField(max_length=120)
    permissions = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    is_default = models.PositiveIntegerField()
    created_by = models.PositiveBigIntegerField()
    updated_by = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "roles"


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = "sessions"


class Settings(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(unique=True, max_length=191)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "settings"


class SimpleSliderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    simple_slider_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=191, blank=True, null=True)
    image = models.CharField(max_length=191)
    link = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "simple_slider_items"


class SimpleSliders(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    key = models.CharField(max_length=120)
    description = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "simple_sliders"


class Slugs(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=191)
    reference_id = models.PositiveBigIntegerField()
    reference_type = models.CharField(max_length=191)
    prefix = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "slugs"


class SlugsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "slugs_id")
    lang_code = models.CharField(max_length=20)
    slugs_id = models.PositiveBigIntegerField()
    key = models.CharField(max_length=191, blank=True, null=True)
    prefix = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "slugs_translations"


class SocialLogins(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.CharField(max_length=191)
    user_id = models.PositiveBigIntegerField()
    provider = models.CharField(max_length=191)
    provider_id = models.CharField(max_length=191)
    token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    token_expires_at = models.DateTimeField(blank=True, null=True)
    provider_data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "social_logins"
        unique_together = (("provider", "provider_id"),)


class States(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.CharField(unique=True, max_length=120, blank=True, null=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    country_id = models.PositiveBigIntegerField(blank=True, null=True)
    order = models.IntegerField()
    image = models.CharField(max_length=191, blank=True, null=True)
    is_default = models.PositiveIntegerField()
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "states"


class StatesTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "states_id")
    lang_code = models.CharField(max_length=20)
    states_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.CharField(max_length=120, blank=True, null=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "states_translations"


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    author_id = models.PositiveBigIntegerField(blank=True, null=True)
    author_type = models.CharField(max_length=191)
    description = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tags"


class TagsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "tags_id")
    lang_code = models.CharField(max_length=20)
    tags_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tags_translations"


class Testimonials(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    content = models.TextField()
    image = models.CharField(max_length=191, blank=True, null=True)
    company = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "testimonials"


class TestimonialsTranslations(models.Model):
    pk = models.CompositePrimaryKey("lang_code", "testimonials_id")
    lang_code = models.CharField(max_length=20)
    testimonials_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "testimonials_translations"


class UserMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=120, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    user_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_meta"


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=191)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=120, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    username = models.CharField(unique=True, max_length=60, blank=True, null=True)
    avatar_id = models.PositiveBigIntegerField(blank=True, null=True)
    super_user = models.IntegerField()
    manage_supers = models.IntegerField()
    permissions = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "users"


class Widgets(models.Model):
    id = models.BigAutoField(primary_key=True)
    widget_id = models.CharField(max_length=120)
    sidebar_id = models.CharField(max_length=120)
    theme = models.CharField(max_length=120)
    position = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "widgets"
