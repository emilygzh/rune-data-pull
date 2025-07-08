from runeq import initialize
from runeq.resources.user import get_current_user

initialize()
my_user = get_current_user()
print(my_user)
print('Active Org:', my_user.active_org_name)



