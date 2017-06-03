import android.graphics.Bitmap;
import android.graphics.BitmapFactory;

import java.io.File;
import java.util.ArrayList;

public class Palette {
  int thresh = 50; //defines the maximum difference in pixel values the program will detect
  int[] imageData; //initialise the variable to hold the raw image data
  ArrayList<Pixel> hist = new ArrayList<>(); //initialise the histogram

  public Palette(Bitmap bmp) {
    createImg(bmp);
  }

  public Palette(String file){
    Bitmap bmp = BitmapFactory.decodeFile(new File(file).toString());
    createImg(bmp);
  }

  private void createImg(Bitmap image) {
    try {
      image = Bitmap.createScaledBitmap(image, 200, 200, true);
      int w = image.getWidth();
      int h = image.getHeight();

      int[] imageData = new int[w*h];
      image.getPixels(imageData, 0, w, 0, 0, w, h);

      System.out.println("for loop");
      for (int i = 0; i < imageData.length; i++){ //loop that finds unique pixels and gathers frequency data
        int tmp = imageData[i]; //initialise a new Pixel
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
    ArrayList<Pixel> record = new ArrayList<Pixel>(); //set up a temporary record to hold similar pixels

    //Pixel comparison = hist.get(0); //get the pixel to compare with
    Pixel highestFreq = hist.get(0);
    for (Pixel pix : hist){ //find the pixel with the highest frequency
      if (pix.frequency > highestFreq.frequency) {
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
        if (hist.get(i).getColor() == pix.getColor()){
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
