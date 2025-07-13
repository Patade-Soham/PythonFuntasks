public class BankAccount {
    private String accountNumber;
    private double balance;

    // Getter and Setter
    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accNum) {
        this.accountNumber = accNum;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double bal) {
        if (bal >= 0) {
            this.balance = bal;
        } else {
            System.out.println("Invalid balance amount.");
        }
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.setAccountNumber("123456789");
        account.setBalance(5000.75);

        System.out.println("Account Number: " + account.getAccountNumber());
        System.out.println("Balance: ₹" + account.getBalance());
    }
}
