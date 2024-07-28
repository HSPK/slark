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
    read_multi_range_data = (
        "/sheets/v2/spreadsheets/{spreadsheetToken}/values_batch_get"
    )
    write_single_range_data = "/sheets/v2/spreadsheets/{spreadsheetToken}/values"
    write_multi_range_data = (
        "/sheets/v2/spreadsheets/{spreadsheetToken}/values_batch_update"
    )


@final
class SPREADSHEETS:
    get_spreadsheet_info = "/sheets/v3/spreadsheets/{spreadsheet_token}"
    get_all_worksheets = "/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/query"
    get_worksheet_info = "/sheets/v3/spreadsheets/{spreadsheet_token}/sheets/{sheet_id}"
    data = WORKSHEET_DATA


@final
class API_PATH:
    knowledge_space = KNOWLEDGE_SPACE
    auth = AUTH
    spreadsheets = SPREADSHEETS
