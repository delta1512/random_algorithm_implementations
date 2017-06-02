import java.awt.Color;
import java.util.ArrayList;

public class Pixel{
  Color colour;
  Integer frequency = 0;
  ArrayList<Double> RGBarr = new ArrayList<Double>();
  public Pixel(Color pixInfo){
    colour = pixInfo;
    RGBarr.add((double) colour.getRed());
    RGBarr.add((double) colour.getGreen());
    RGBarr.add((double) colour.getBlue());
  }
  public boolean compare(Color comparison){
    if (colour.equals(comparison)) {
      frequency += 1;
      return true;
    } else {
      return false;
    }
  }
  public double findEuclideanDist(ArrayList<Double> pix){
    double sum = 0.0;
    for (int i = 0; i < 3; i++){
      sum += Math.pow((RGBarr.get(i) - pix.get(i)), 2.0);
    }
    return Math.sqrt(sum);
  }
}
