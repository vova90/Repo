public abstract class AbstractCar {

    protected String name = "Abstract car";

    // abstract method is a method without a body
    // each class extending this abstract class must implement this method
    protected abstract void drive();

    // this method will be common for all of the child classes
    protected void stop(){
        System.out.println("Car stopped");
    }
}