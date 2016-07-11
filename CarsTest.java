package abstract_classes;

public class CarsTest {

    public static void main(String[] args) {
        SportCar sportCar = new SportCar();

        sportCar.drive();
        sportCar.stop();

        Lorry lorry = new Lorry();

        lorry.drive();
        lorry.stop();
    }
}
