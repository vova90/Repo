package abstract_classes;

public class SportCar extends AbstractCar {

    // this is a constructor - a method, that gets called every time a new SportCar object is created
    public SportCar() {
        // where does this variable come from ?
        name = "Sport car";
    }

    @Override
    protected void drive() {
        System.out.println(name + " is driving");
    }
}
