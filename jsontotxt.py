import json

labels = ['person','bike','car','motor','bus','train','truck','light','hydrant','sign','dog','skateboard','stroller','scooter','other vehicle']
labelmap = dict(zip(labels,range(15)))
labelmap['rider'] = 0
#labelmap['face'] = 0
labelmap['traffic light'] = 7

def convert(name):
    count = 0
    with open("jsonlabel/"+name+".json","r") as f:
        dict = json.load(f)
    for img in dict['frames']:
        imgh,imgw = img['height'],img['width']
        with open("labels/"+name+'/video-'+img['videoMetadata']['videoId']+"-frame-"+str(img['videoMetadata']['frameIndex']).zfill(6)+"-"+img['datasetFrameId']+".txt","w") as f:
            for box in img["annotations"]:
                #if len(box['labels']) > 1:
                #    print(box['labels'])
                #print(box)
                labeltxt = box['labels'][0]
                if labeltxt not in ['license plate','face']:
                    label = labelmap[labeltxt]
                else:
                    continue
                #try:
                #    label = labelmap[labeltxt]
                #except KeyError:
                #    label = 14
                dim = box['boundingBox']
                x = (dim['x'] + (dim['w']/2))/imgw
                y = (dim['y'] + (dim['h']/2))/imgh
                w = dim['w']/imgw
                h = dim['h']/imgh
                line = [label,x,y,w,h]
                line = [str(i) for i in line]
                line = " ".join(line)
                f.write(line+"\n")

convert("train")
convert("val")
