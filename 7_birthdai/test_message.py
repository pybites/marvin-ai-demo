import pytest
from message import send_whatsapp_message


@pytest.mark.parametrize("text, telephone_number_sender, telephone_number_receiver", [
    ("Hey there!", "+", "+"),
])
def test_send_whatsapp_message(text, telephone_number_sender, telephone_number_receiver):
    send_whatsapp_message(text=text, telephone_number_sender=telephone_number_sender, 
                          telephone_number_receiver=telephone_number_receiver)
