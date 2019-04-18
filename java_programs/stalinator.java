import java.util.Scanner;

public class stalinator {
    public static void line_break() {
	for (int i = 0; i < 88; i++) {
	    System.out.print("-");
        }
	System.out.print("\n");
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Stalinator Economic Planning ");
        System.out.print("Tool v.3 - Coded in Java by ");
        System.out.print("Dante Falzone\n");

        System.out.print("Input the resource to be calculated");
        System.out.print(" and press ENTER.\n");
        String resource = input.nextLine();

        System.out.print("Input the units of measurement for ");
        System.out.print("that resource and press ENTER. (e.");
        System.out.print("g. kg, L, etc.)\n");
        String units = input.nextLine();

        System.out.print("Input the projected demand for that ");
        System.out.print("resource as a number and press ");
        System.out.print("ENTER.\n");
        System.out.print(units + " ");
        float demand = input.nextFloat();

        System.out.print("Input the current supply for that ");
	System.out.print("resource as a number and press ");
	System.out.print("ENTER.\n");
	System.out.print(units + " ");
	float supply = input.nextFloat();

	System.out.print("Input the estimated cost per unit ");
	System.out.print("to produce that resource and press");
	System.out.print("ENTER.\n");
	System.out.print("$ ");
	float cost = input.nextFloat();

        System.out.println("Generating economic planning report...");

	float price = ((cost * demand) / supply);

        float sh = supply - demand;

        float abssh;
	if (sh < 0) {
	    abssh = (sh - (2 * sh));
	} else {
            abssh = sh;
	}

        System.out.println("Finished.");

	stalinator.line_break();
	System.out.println("Economic planning report");
	stalinator.line_break();
        System.out.println(">> Product: " + resource);
        System.out.println(">> Production volume: " + supply + " " + units);
	System.out.println(">> Projected demand: "  + demand + " " + units);
        System.out.println(">> Ideal price: $ " + price);
	System.out.print("Resource scarcity status: ");
	if (sh > 0) {
            System.out.println("surplus");
	} else if (sh == 0) {
	    System.out.println("low supply, but no shortage");
	} else {
	    System.out.println("shortage - recommend increasing supply by " + abssh + " " + units);
	}
        stalinator.line_break();

	/* I find Java to be a very verbose language.
           Compare:
               C:          printf("%s\n", x);
               C++:        cout << x << '\n';
               Python:     print(x)
               Javascript: console.log(x);
               Java:       System.out.println(x);     */
    }
}
