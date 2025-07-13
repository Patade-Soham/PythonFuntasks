public class Student {
    String name;
    int rollNo;

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
    }

    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "Alice";
        s1.rollNo = 101;

        Student s2 = new Student();
        s2.name = "Bob";
        s2.rollNo = 102;

        s1.display();
        System.out.println();
        s2.display();
    }
}
