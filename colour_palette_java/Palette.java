import java.io.File;
import java.awt.Color;
import java.awt.Graphics2D;
import java.util.ArrayList;
import javax.imageio.ImageIO;
import java.awt.RenderingHints;
import java.awt.image.BufferedImage;

public class Palette {
  int thresh = 50; //defines the maximum difference in pixel values the program will detect
  int[] imageData; //initialise the variable to hold the raw image data
  ArrayList<Pixel> hist = new ArrayList<Pixel>(); //initialise the histogram
  public Palette(String file){
    try {
      BufferedImage image = ImageIO.read(new File(file)); //load image into a buffer
      int w = image.getWidth();
      int h = image.getHeight();
      if (w*h > 40000){ //if the image is bigger than 200x200...
        BufferedImage tmp = new BufferedImage(200, 200, BufferedImage.TYPE_INT_ARGB);
        Graphics2D tempGraphics = tmp.createGraphics();
        tempGraphics.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BICUBIC);
        tempGraphics.drawImage(image, 0, 0, 200, 200, null);
        tempGraphics.dispose();
        image = tmp; //...resize
        //update sizes
        w = image.getWidth();
        h = image.getHeight();
      }
      imageData = image.getRGB(0, 0, w, h, null, 0, w);
      for (int i = 0; i < imageData.length; i++){ //loop that finds unique pixels and gathers frequency data
        Color tmp = new Color(imageData[i]); //initialise a new Pixel
        boolean found = false;
        for (Pixel pix : hist){ //search the histogram...
          if (pix.compare(tmp)){ //for the same colours
            found = true;
            break;
          }
        }
        if (!found){ //if a unique colour was found...
          hist.add(new Pixel(tmp)); //make a new entry in the histogram
        }
      }
    } catch (Exception err){err.printStackTrace();}
  }

  public short[] getColour(){
    //int freqResult; //debug
    ArrayList<Pixel> record = new ArrayList<Pixel>(); //set up a temporary record to hold similar pixels
    //Pixel comparison = hist.get(0); //get the pixel to compare with
    Pixel highestFreq = hist.get(0);
    for (Pixel pix : hist){ //find the pixel with the highest frequency
      if (pix.frequency > highestFreq.frequency){
        highestFreq = pix;
      }
    }
    Pixel comparison = highestFreq; //make it the comparison pixel
    record.add(comparison); //add it to the record
    for (int i = 0; i < hist.size(); i++){ //find all the pixels that are similar to the comparison one...
      Pixel pix = hist.get(i);
      if (comparison.findEuclideanDist(pix.RGBarr) < thresh){ //based on the euclidean distance threshold
        record.add(pix); //if it's similar, add it to the record
      }
    }
    //int sum = 0; //debug
    int[] sumPix = {0, 0, 0};
    for (Pixel pix : record){
      //sum += pix.frequency; //debug
      for (int i = 0; i < 3; i++){ //add the values of each RGB to the sum
        sumPix[i] += pix.RGBarr.get(i);
      }
      for (int i = 0; i < hist.size(); i++){ //remove the pixel from the main histogram
        if (hist.get(i).colour.equals(pix.colour)){
          hist.remove(i);
        }
      }
    }
    //int av = Math.round(sum / record.size()); //debug
    short[] avPix = new short[3];
    for (int i = 0; i < 3; i++){ //get the average pixel value
      avPix[i] = (short) Math.round(sumPix[i] / record.size());
    }
    //freqResult = av; //debug
    //System.out.println(freqResult); //debug
    return avPix; //send out the picked colour
  }
}
