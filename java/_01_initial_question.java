import java.util.function.Consumer;
import java.util.ArrayList;
import java.lang.Runnable;

public class _01_initial_question {
    // java compile will not even let this code compile
    public static void main(String[] args) {

        ArrayList<Runnable> funcs = new ArrayList<>();

        for (int i=0; i<10; i++) {
            funcs.add(() -> System.out.println(Integer.toString(i)));
        }

        for (Runnable r : funcs) r.run();
    }

}