
class Klasa1 
{
    public static void main(String[] args) 
    {
        new Klasa4().funkcija2();
    }
}

class Klasa2 
{
    public static void main(String[] args) 
    {
        new Klasa5().funkcija1();
        new Klasa4().funkcija2();
    }
}

class Klasa4 
{
    void funkcija2()
    {
        System.out.println("Klasa4.funkcija2");
    }
}