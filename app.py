import streamlit as st

# Account Class (OOP)
class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def debit(self, amount):
        if amount <= 0:
            return "Enter a valid amount"
        elif amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Rs. {amount} debited successfully"

    def credit(self, amount):
        if amount <= 0:
            return "Enter a valid amount"
        else:
            self.balance += amount
            return f"Rs. {amount} credited successfully"

    def get_balance(self):
        return self.balance


# Page configuration
st.set_page_config(
    page_title="Bank Account Management System",
    page_icon="🏦",
    layout="centered"
)

# Initialize account
if "user1" not in st.session_state:
    st.session_state.user1 = Account(12345, 12560)

if "message" not in st.session_state:
    st.session_state.message = "Welcome to our Bank!"

user1 = st.session_state.user1

# Application heading
st.title("🏦 Bank Account Management System")
st.caption("Python OOP Based Banking Simulation")

st.divider()

# Account details
st.subheader("Account Details")
st.write("Account Number:", user1.account)

st.metric(
    label="Current Balance",
    value=f"₹ {user1.get_balance():,.2f}"
)

st.divider()

# Deposit section
st.subheader("💰 Deposit Money")

with st.form("deposit_form"):
    deposit_amount = st.number_input(
        "Enter deposit amount (₹)",
        min_value=0.0,
        step=100.0
    )
    deposit_button = st.form_submit_button("Deposit")

    if deposit_button:
        st.session_state.message = user1.credit(deposit_amount)

# Withdrawal section
st.subheader("💸 Withdraw Money")

with st.form("withdraw_form"):
    withdraw_amount = st.number_input(
        "Enter withdrawal amount (₹)",
        min_value=0.0,
        step=100.0
    )
    withdraw_button = st.form_submit_button("Withdraw")

    if withdraw_button:
        st.session_state.message = user1.debit(withdraw_amount)

# Transaction message
st.divider()
st.subheader("Transaction Status")
st.info(st.session_state.message)

# Refresh balance
st.metric(
    label="Updated Balance",
    value=f"₹ {user1.get_balance():,.2f}"
)

st.caption("This is an educational banking simulation project.")
st.caption("Developed by Abhinandan Kumar Maurya")
