from typing import final


@final
class KNOWLEDGE_SPACE_NODE:
    get_node = "/wiki/v2/spaces/get_node"


@final
class KNOWLEDGE_SPACE:
    nodes = KNOWLEDGE_SPACE_NODE


@final
class AUTH:
    get_tenant_access_token = "/auth/v3/tenant_access_token/internal"
    get_app_access_token = "/auth/v3/app_access_token/internal"
    get_user_access_token = "/authen/v1/oidc/access_token"


@final
class WORKSHEET_DATA:
    prepend_data = "/sheets/v2/spreadsheets/{spreadsheetToken}/values_prepend"
    append_data = "/sheets/v2/spreadsheets/{spreadsheetToken}/values_append"
    read_single_range_data = "/sheets/v2/spreadsheets/{spreadsheetToken}/values/{range}"
    read_multi_range_data = "/sheets/v2/spreadsheets/{spreadsheetToken}/values_batch_get"
    write_single_range_data = "/sheets/v2/spreadsheets/{spreadsheetToken}/values"
    write_multi_range_data = "/sheets/v2/spreadsheets/{spreadsheetToken}/values_batch_update"


@final
class SPREADSHEETS:
    get_spreadsheet_info = "/sheets/v3/spreadsheets/{spreadsheet_token}"
    get_all_worksheets = "/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/query"
    get_worksheet_info = "/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}"
    data = WORKSHEET_DATA


@final
class BITABLES:
    get_bitable_meta = "/bitable/v1/apps/{app_token}"
    update_bitable_meta = "/bitable/v1/apps/{app_token}"

    create_table = "/bitable/v1/apps/{app_token}/tables"
    batch_create_table = "/bitable/v1/apps/{app_token}/tables/batch_create"
    delete_table = "/bitable/v1/apps/{app_token}/tables/{table_id}"
    batch_delete_table = "/bitable/v1/apps/{app_token}/tables/batch_delete"
    update_table = "/bitable/v1/apps/{app_token}/tables/{table_id}"
    list_tables = "/bitable/v1/apps/{app_token}/tables"

    copy_dashboard = "/bitable/v1/apps/{app_token}/dashboards/{block_id}/copy"
    list_dashboards = "/bitable/v1/apps/{app_token}/dashboards"

    update_view = "/bitable/v1/apps/{app_token}/tables/{table_id}/views/{view_id}"
    get_view_info = "/bitable/v1/apps/{app_token}/tables/{table_id}/views/{view_id}"
    list_views = "/bitable/v1/apps/{app_token}/tables/{table_id}/views"
    create_view = "/bitable/v1/apps/{app_token}/tables/{table_id}/views"
    delete_view = "/bitable/v1/apps/{app_token}/tables/{table_id}/views/{view_id}"

    update_form_meta = "/bitable/v1/apps/{app_token}/tables/{table_id}/forms/{form_id}"
    get_form_meta = "/bitable/v1/apps/{app_token}/tables/{table_id}/forms/{form_id}"
    update_form_field = (
        "/bitable/v1/apps/{app_token}/tables/{table_id}/forms/{form_id}/fields/{field_id}"
    )
    list_form_fileds = "/bitable/v1/apps/{app_token}/tables/{table_id}/forms/{form_id}/fields"

    create_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records"
    update_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    search_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/search"

    get_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    delete_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"

    batch_create_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create"
    batch_update_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_update"
    batch_get_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_get"
    batch_delete_record = "/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_delete"

    list_field = "/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    create_field = "/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    update_field = "/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}"
    delete_field = "/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}"


@final
class DOCUMENTS:
    get_base_info = "/docx/v1/documents/{document_id}"
    get_raw_content = "/docx/v1/documents/{document_id}/raw_content"
    get_blocks = "/docx/v1/documents/{document_id}/blocks"
    create_document = "/docx/v1/documents"

    get_block_content = "/docx/v1/documents/{document_id}/blocks/{block_id}"
    get_children_blocks = "/docx/v1/documents/{document_id}/blocks/{block_id}/children"
    create_block = "/docx/v1/documents/{document_id}/blocks/{block_id}/children"
    update_block = "/docx/v1/documents/{document_id}/blocks/{block_id}"
    batch_update_block = "/docx/v1/documents/{document_id}/blocks/batch_update"
    batch_delete_block = "/docx/v1/documents/{document_id}/blocks/{block_id}/children/batch_delete"


@final
class BOARD:
    download_as_image = "/board/v1/whiteboards/{whiteboard_id}/download_as_image"


@final
class ASSETS:
    download = "/drive/v1/medias/{file_token}/download"


@final
class IMAGE:
    upload = "/im/v1/images"


@final
class MESSAGE:
    send = "im/v1/messages"
    reply = "im/v1/messages/{message_id}/reply"
    edit = "im/v1/messages/{message_id}"
    forward = "im/v1/messages/{message_id}/forward"
    get = "im/v1/messages/{message_id}"
    get_resource = "im/v1/messages/{message_id}/resources/{file_key}"


@final
class API_PATH:
    knowledge_space = KNOWLEDGE_SPACE
    auth = AUTH
    spreadsheets = SPREADSHEETS
    bitables = BITABLES
    documents = DOCUMENTS
    board = BOARD
    assets = ASSETS
    image = IMAGE
    message = MESSAGE
