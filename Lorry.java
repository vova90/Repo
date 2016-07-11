package Repo;

public class Lorry extends AbstractCar {

    // this is a constructor - a method, that gets called every time a new Lorry object is created
    public Lorry() {
        // where does this variable come from ?
        name = "Lorry";
    }

    // try to remove this one and see what happens
    @Override
    protected void drive() {
        System.out.println(name + " is driving");
    }
}
