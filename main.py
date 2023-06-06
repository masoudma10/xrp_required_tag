from xrpl.models import AccountSet, AccountSetFlag
import xrpl
from xrpl.transaction import safe_sign_and_autofill_transaction, send_reliable_submission
from xrpl.wallet import Wallet


url = "https://s1.ripple.com:51234/"
client = xrpl.clients.JsonRpcClient(url)

wallet = Wallet('snfKijZph8BojYpZ8tQD5FVWYujtm', sequence=62871975)


tx = AccountSet(
            account=wallet.classic_address,
            set_flag=AccountSetFlag.ASF_REQUIRE_DEST,
        )

signed_tx = safe_sign_and_autofill_transaction(tx, wallet, client)

print(signed_tx.get_hash())


submit = send_reliable_submission(signed_tx, client)
print(submit)