from petstore_api.paths.user_username.get.operation import ApiForGet
from petstore_api.paths.user_username.put.operation import ApiForPut
from petstore_api.paths.user_username.delete.operation import ApiForDelete


class UserUsername(
    ApiForGet,
    ApiForPut,
    ApiForDelete,
):
    pass
