import java.util.function.Consumer;
import java.util.ArrayList;
import java.lang.Runnable;

public class _11_quiz {

    public static void main(String[] args) {

        ArrayList<Runnable> funcs = new ArrayList<>();

        for (int i=0; i<10; i++) {
            final int j = i;
            funcs.add(() -> System.out.println(Integer.toString(j)));
        }

        for (Runnable r : funcs) r.run();
    }

}