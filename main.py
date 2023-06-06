from xrpl.models import AccountSet, AccountSetFlag
import xrpl
from xrpl.transaction import safe_sign_and_autofill_transaction, send_reliable_submission
from xrpl.wallet import Wallet


url = "https://s1.ripple.com:51234/"
client = xrpl.clients.JsonRpcClient(url)


def required_tag(private, address):
    wallet = Wallet(private, sequence=62871975)

    tx = AccountSet(
                account=wallet.classic_address,
                set_flag=AccountSetFlag.ASF_REQUIRE_DEST,
            )
    signed_tx = safe_sign_and_autofill_transaction(tx, wallet, client)
    submit = send_reliable_submission(signed_tx, client)
    return submit