public class Caja {

    private int ancho;
    private int alto;
    private int profundidad;

    public Caja(){
        this.ancho = 0;
        this.alto = 0;
        this.profundidad=0;
    }

    public Caja(int ancho,int alto,int profundidad){
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad=profundidad;
    }

    public int getAncho()          { return ancho; }
    public int getAlto()          { return alto; }
    public int getProfundidad()   { return profundidad; }

    public void setAncho(int a)          { this.ancho = a; }
    public void setAlto(int h)          { this.alto = h; }
    public void setProfundidad(int p)   { this.profundidad = p; }

    public int volumen() {
        return ancho * alto * profundidad;
    }
}
