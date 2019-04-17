public class Main {
    public static void main(String[] args) {
        int middle = 3110;
        char comma = ',';
        System.out.println("H" + middle + comma + " world!");
        My_function.my_func();
        // Wow, so *everything* in Java has to be part of a class? Wild.
        /* * * * * * * { Scale of object-orientedness} * * * * * * * * * *
         *                                                               *
         *        C       C++   Javascript     Python         Java       *
         * less<--|--------|--------|------------|--------------|-->more *
         *                                                               *
         * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
    }
}

public class My_function {
    public static void my_func() {
        System.out.println("This is Dante's phantastic phunction call.");
    }
}
