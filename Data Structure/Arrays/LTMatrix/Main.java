class LowerTriangularMatrix {

    private int n;
    private int[] arr;

    // Constructor
    public LowerTriangularMatrix(int n) {
        this.n = n;
        this.arr = new int[n * (n + 1) / 2];
    }

    // Set value
    public void set(int i, int j, int value) {

        if (i >= j) {
            int index = i * (i + 1) / 2 + j;
            arr[index] = value;
        } 
        else if (value != 0) {
            System.out.println(
                "Cannot store a non-zero value above the main diagonal."
            );
        }
    }

    // Get value
    public int get(int i, int j) {

        if (i >= j) {
            int index = i * (i + 1) / 2 + j;
            return arr[index];
        }

        return 0;
    }

    // Display matrix
    public void display() {

        for (int i = 0; i < n; i++) {

            for (int j = 0; j < n; j++) {
                System.out.print(get(i, j) + " ");
            }

            System.out.println();
        }
    }

    // Getter for arr
    public int[] getArray() {
        return arr;
    }
}


public class Main {

    public static void main(String[] args) {

        LowerTriangularMatrix lt = new LowerTriangularMatrix(3);

        lt.set(0, 0, 1);
        lt.set(1, 0, 2);
        lt.set(1, 1, 3);
        lt.set(2, 0, 4);
        lt.set(2, 1, 5);
        lt.set(2, 2, 6);

        // Display matrix
        lt.display();

        // Get a particular value
        System.out.println("Value at index i, j:");
        System.out.println(lt.get(2, 2));

        // Display internal 1D array
        System.out.print("Array: ");

        for (int value : lt.getArray()) {
            System.out.print(value + " ");
        }
    }
}