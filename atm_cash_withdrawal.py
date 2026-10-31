"""Streamlit ATM withdrawal simulator."""

from decimal import Decimal, InvalidOperation

import streamlit as st


DEMO_PIN = "1234"
INITIAL_BALANCE = Decimal("5000.00")
MAX_PIN_ATTEMPTS = 3


def format_money(amount: Decimal) -> str:
    return f"Rs. {amount:,.2f}"


def reset_simulation() -> None:
    st.session_state["balance"] = INITIAL_BALANCE
    st.session_state["pin_attempts"] = 0
    st.session_state["authenticated"] = False
    st.session_state["card_blocked"] = False
    st.session_state["pin_entry"] = ""
    st.session_state["withdrawal_entry"] = ""
    st.session_state["withdrawal_result"] = None


st.set_page_config(page_title="ATM cash withdrawal", page_icon="🏧")

st.session_state.setdefault("balance", INITIAL_BALANCE)
st.session_state.setdefault("pin_attempts", 0)
st.session_state.setdefault("authenticated", False)
st.session_state.setdefault("card_blocked", False)
st.session_state.setdefault("pin_entry", "")
st.session_state.setdefault("withdrawal_entry", "")
st.session_state.setdefault("withdrawal_result", None)

st.title("ATM cash withdrawal")
st.caption("Demo simulation only. Use PIN 1234; this is not real ATM security.")

if not st.session_state["authenticated"]:
    st.subheader("Step 1: Verify your PIN")

    if st.session_state["card_blocked"]:
        st.error("Your card is blocked after three incorrect PIN attempts.")
    else:
        with st.form("pin_form"):
            pin = st.text_input(
                "Enter your 4-digit PIN",
                type="password",
                max_chars=4,
                key="pin_entry",
            )
            pin_submitted = st.form_submit_button("Verify PIN", type="primary")

        if pin_submitted:
            if pin == DEMO_PIN:
                st.session_state["authenticated"] = True
                st.session_state["withdrawal_result"] = None
                st.rerun()

            st.session_state["pin_attempts"] += 1
            if st.session_state["pin_attempts"] >= MAX_PIN_ATTEMPTS:
                st.session_state["card_blocked"] = True
                st.rerun()
            else:
                remaining = MAX_PIN_ATTEMPTS - st.session_state["pin_attempts"]
                st.error(f"Incorrect PIN. {remaining} attempt(s) remaining.")
        elif st.session_state["pin_attempts"]:
            remaining = MAX_PIN_ATTEMPTS - st.session_state["pin_attempts"]
            st.info(f"You have {remaining} PIN attempt(s) remaining.")

    st.button("Restart simulation", on_click=reset_simulation)
    st.stop()

st.subheader("Step 2: Withdraw cash")
st.metric("Available balance", format_money(st.session_state["balance"]))

with st.form("withdrawal_form"):
    amount_text = st.text_input(
        "Withdrawal amount (Rs.)",
        key="withdrawal_entry",
        placeholder="For example, 1000",
    )
    withdrawal_submitted = st.form_submit_button(
        "Withdraw cash",
        type="primary",
    )

if withdrawal_submitted:
    try:
        amount = Decimal(amount_text.strip())
    except InvalidOperation:
        st.session_state["withdrawal_result"] = (
            "error",
            "Please enter a valid withdrawal amount.",
        )
    else:
        if not amount.is_finite() or amount <= 0:
            st.session_state["withdrawal_result"] = (
                "error",
                "Withdrawal amount must be greater than zero.",
            )
        elif amount > st.session_state["balance"]:
            st.session_state["withdrawal_result"] = (
                "error",
                "Insufficient balance. No cash was dispensed.",
            )
        else:
            st.session_state["balance"] -= amount
            st.session_state["withdrawal_result"] = (
                "success",
                f"Please collect your cash: {format_money(amount)}",
            )
    st.rerun()

if st.session_state["withdrawal_result"]:
    result_type, result_message = st.session_state["withdrawal_result"]
    if result_type == "success":
        st.success(result_message)
    else:
        st.error(result_message)

st.button("Restart simulation", on_click=reset_simulation)
