'''import cv2
import os

def annotate_images(folder_path, output_file):
    annotations = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp','.JPEG','.JPG')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Display the image and let the user annotate it
            cv2.imshow('Image Annotation', image)
            print("Annotate the image by drawing a rectangle around the object of interest.")
            print("Press 's' to skip, 'q' to quit, or any other key to proceed.")
            k = cv2.waitKey(0)

            if k == ord('q'):
                break
            elif k == ord('s'):
                continue
            else:
                # Get the coordinates of the bounding box
                bbox = cv2.selectROI('Image Annotation', image, fromCenter=False, showCrosshair=True)
                cv2.destroyAllWindows()

                # Add the annotation to the list
                annotation = {
                    'image_path': image_path,
                    'x': int(bbox[0]),
                    'y': int(bbox[1]),
                    'width': int(bbox[2]),
                    'height': int(bbox[3])
                }
                annotations.append(annotation)

    # Save the annotations to a .txt file
    with open(output_file, 'w') as f:
        for annotation in annotations:
            line = f"{annotation['image_path']} {annotation['x']} {annotation['y']} {annotation['width']} {annotation['height']}\n"
            f.write(line)

    print(f"Annotations saved to {output_file}")

if __name__ == "__main__":
    input_folder = "/home/rguktrkvalley/Music/Buf_cow_cascade/n1"  # Replace with the path to your input image folder
    output_txt_file = "/home/rguktrkvalley/Music/Buf_cow_cascade/n1annotations.txt"  # Replace with the desired output .txt file name

    annotate_images(input_folder, output_txt_file)
import cv2
import os

def annotate_images(folder_path, output_file):
    annotations = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Function to handle mouse events
            def mouse_callback(event, x, y, flags, param):
                nonlocal image, bbox
                if event == cv2.EVENT_LBUTTONDOWN:
                    bbox = (x, y, 0, 0)
                elif event == cv2.EVENT_LBUTTONUP:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])

            # Create a window and set the mouse callback function
            cv2.namedWindow('Image Annotation')
            cv2.setMouseCallback('Image Annotation', mouse_callback)
            bbox = (0, 0, 0, 0)

            while True:
                # Display the image and the rectangle
                annotated_image = image.copy()
                cv2.rectangle(annotated_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                cv2.imshow('Image Annotation', annotated_image)
                print("Annotate the image by dragging a rectangle around the object of interest.")
                print("Press 's' to skip, 'q' to quit, or any other key to proceed.")
                k = cv2.waitKey(1)

                if k == ord('q'):
                    break
                elif k == ord('s'):
                    break
                elif k != -1:
                    # Add the annotation to the list
                    annotation = {
                        'image_path': image_path,
                        'x': bbox[0],
                        'y': bbox[1],
                        'width': bbox[2],
                        'height': bbox[3]
                    }
                    annotations.append(annotation)

    # Save the annotations to a .txt file
    with open(output_file, 'w') as f:
        for annotation in annotations:
            line = f"{annotation['image_path']} {annotation['x']} {annotation['y']} {annotation['width']} {annotation['height']}\n"
            f.write(line)

    print(f"Annotations saved to {output_file}")

if __name__ == "__main__":
    input_folder = "/home/rguktrkvalley/Music/Buf_cow_cascade/n"  # Replace with the path to your input image folder
    output_txt_file = "/home/rguktrkvalley/Music/Buf_cow_cascade/n1annotations.txt"  # Replace with the desired output .txt file name

    annotate_images(input_folder, output_txt_file)

import cv2
import os

def annotate_images(folder_path, output_file):
    annotations = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Function to handle mouse events
            def mouse_callback(event, x, y, flags, param):
                nonlocal image, bbox
                if event == cv2.EVENT_LBUTTONDOWN:
                    bbox = (x, y, 0, 0)
                elif event == cv2.EVENT_LBUTTONUP:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])

            # Create a window and set the mouse callback function
            cv2.namedWindow('Image Annotation')
            cv2.setMouseCallback('Image Annotation', mouse_callback)
            bbox = (0, 0, 0, 0)

            while True:
                # Display the image and the rectangle
                annotated_image = image.copy()
                cv2.rectangle(annotated_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                cv2.imshow('Image Annotation', annotated_image)
                print("Annotate the image by dragging a rectangle around the object of interest.")
                print("Press 's' to skip, 'q' to quit, or any other key to proceed and save the annotation.")
                k = cv2.waitKey(1)

                if k == ord('q'):
                    break
                elif k == ord('s'):
                    break
                elif k != -1:
                    # Add the annotation to the list
                    annotation = {
                        'image_path': image_path,
                        'x': bbox[0],
                        'y': bbox[1],
                        'width': bbox[2],
                        'height': bbox[3]
                    }
                    annotations.append(annotation)
                    print(annotation)
                    print("HI hello")
                    break

    # Save the annotations to a .txt file
    with open(output_file, 'w') as f:
        for annotation in annotations:
            line = f"{annotation['image_path']} {annotation['x']} {annotation['y']} {annotation['width']} {annotation['height']}\n"
            f.write(line)

    print(f"Annotations saved to {output_file}")

if __name__ == "__main__":
    input_folder = "/home/rguktrkvalley/Music/Buf_cow_cascade/n"  # Replace with the path to your input image folder
    output_txt_file = "/home/rguktrkvalley/Music/Buf_cow_cascade/n1annotations.txt"  # Replace with the desired output .txt file name

    annotate_images(input_folder, output_txt_file)'''
'''import cv2
import os

def annotate_images(folder_path, output_file):
    annotations = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Function to handle mouse events
            def mouse_callback(event, x, y, flags, param):
                nonlocal image, bbox, annotate_image
                if event == cv2.EVENT_LBUTTONDOWN:
                    bbox = (x, y, 0, 0)
                elif event == cv2.EVENT_LBUTTONUP:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                    cv2.rectangle(annotate_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                    cv2.imshow('Image Annotation', annotate_image)
                elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                    annotate_image = image.copy()
                    cv2.rectangle(annotate_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                    cv2.imshow('Image Annotation', annotate_image)

            # Create a window and set the mouse callback function
            cv2.namedWindow('Image Annotation')
            cv2.setMouseCallback('Image Annotation', mouse_callback)
            bbox = (0, 0, 0, 0)
            annotate_image = image.copy()

            while True:
                # Display the image and the rectangle
                cv2.imshow('Image Annotation', annotate_image)
                print("Annotate the image by dragging a rectangle around the object of interest.")
                print("Press 's' to skip, 'q' to quit, or any other key to proceed and save the annotation.")
                k = cv2.waitKey(1)

                if k == ord('q'):
                    break
                elif k == ord('s'):
                    continue
                elif k != -1:
                    # Add the annotation to the list
                    annotation = {
                        'image_path': image_path,
                        'x': bbox[0],
                        'y': bbox[1],
                        'width': bbox[2],
                        'height': bbox[3]
                    }
                    annotations.append(annotation)
                    print(annotation)

                    # Reset the image and bounding box for the next annotation
                    annotate_image = image.copy()
                    bbox = (0, 0, 0, 0)
                    cv2.imshow('Image Annotation', annotate_image)

            # Close the window after 'q' is pressed
            cv2.destroyWindow('Image Annotation')

    # Save the annotations to a .txt file
    with open(output_file, 'w') as f:
        for annotation in annotations:
            line = f"{annotation['image_path']} {annotation['x']} {annotation['y']} {annotation['width']} {annotation['height']}\n"
            f.write(line)

    print(f"Annotations saved to {output_file}")

if __name__ == "__main__":
    input_folder = "/home/rguktrkvalley/Music/Buf_cow_cascade/n"  # Replace with the path to your input image folder
    output_txt_file = "/home/rguktrkvalley/Music/Buf_cow_cascade/n1annotations.txt"  # Replace with the desired output .txt file name

    annotate_images(input_folder, output_txt_file)'''
'''
import cv2
import os

def annotate_images(folder_path, output_file):
    annotations = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Function to handle mouse events
            def mouse_callback(event, x, y, flags, param):
                nonlocal image, bbox, annotate_image
                if event == cv2.EVENT_LBUTTONDOWN:
                    bbox = (x, y, 0, 0)
                elif event == cv2.EVENT_LBUTTONUP:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                    cv2.rectangle(annotate_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                    cv2.imshow('Image Annotation', annotate_image)
                elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                    annotate_image = image.copy()
                    cv2.rectangle(annotate_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                    cv2.imshow('Image Annotation', annotate_image)

            # Create a window and set the mouse callback function
            cv2.namedWindow('Image Annotation')
            cv2.setMouseCallback('Image Annotation', mouse_callback)
            bbox = (0, 0, 0, 0)
            annotate_image = image.copy()

            while True:
                # Display the image and the rectangle
                cv2.imshow('Image Annotation', annotate_image)
                print("Annotate the image by dragging a rectangle around the object of interest.")
                print("Press 's' to skip, 'q' to quit, or any other key to proceed and save the annotation.")
                k = cv2.waitKey(0)

                if k == ord('q'):
                    break
                elif k == ord('s'):
                    continue
                elif k != -1:
                    # Add the annotation to the list
                    annotation = {
                        'image_path': image_path,
                        'x': bbox[0],
                        'y': bbox[1],
                        'width': bbox[2],
                        'height': bbox[3]
                    }
                    annotations.append(annotation)
                    print(annotation)

                    # Reset the image and bounding box for the next annotation
                    annotate_image = image.copy()
                    bbox = (0, 0, 0, 0)
                    cv2.imshow('Image Annotation', annotate_image)
                    break

            # Close the window after 'q' is pressed
            cv2.destroyWindow('Image Annotation')

    # Save the annotations to a .txt file
    with open(output_file, 'w') as f:
        for annotation in annotations:
            line = f"{annotation['image_path']} {annotation['x']} {annotation['y']} {annotation['width']} {annotation['height']}\n"
            f.write(line)

    print(f"Annotations saved to {output_file}")

if __name__ == "__main__":
    input_folder = "/home/rguktrkvalley/Music/Buf_cow_cascade/n"  # Replace with the path to your input image folder
    output_txt_file = "/home/rguktrkvalley/Music/Buf_cow_cascade/n1annotations.txt"  # Replace with the desired output .txt file name

    annotate_images(input_folder, output_txt_file)'''
import cv2
import os

def annotate_images(folder_path, output_file):
    annotations = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp','.JPEG','.JPG','.PNG')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Function to handle mouse events
            def mouse_callback(event, x, y, flags, param):
                nonlocal image, bbox, annotate_image
                if event == cv2.EVENT_LBUTTONDOWN:
                    bbox = (x, y, 0, 0)
                elif event == cv2.EVENT_LBUTTONUP:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                    cv2.rectangle(annotate_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                    cv2.imshow('Image Annotation', annotate_image)
                elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
                    bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
                    annotate_image = image.copy()
                    cv2.rectangle(annotate_image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
                    cv2.imshow('Image Annotation', annotate_image)

            # Create a window and set the mouse callback function
            cv2.namedWindow('Image Annotation')
            cv2.setMouseCallback('Image Annotation', mouse_callback)
            bbox = (0, 0, 0, 0)
            annotate_image = image.copy()

            while True:
                # Display the image and the rectangle
                cv2.imshow('Image Annotation', annotate_image)
                print("Annotate the image by dragging a rectangle around the object of interest.")
                print("Press 's' to skip, 'q' to quit, or any other key to proceed and save the annotation.")
                k = cv2.waitKey(0)

                if k == ord('q'):
                    break
                elif k == ord('s'):
                    continue
                elif k != -1:
                    # Add the annotation to the list
                    annotation = f"{image_path} 1 {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}"
                    annotations.append(annotation)
                    print(annotation)

                    # Reset the image and bounding box for the next annotation
                    annotate_image = image.copy()
                    bbox = (0, 0, 0, 0)
                    cv2.imshow('Image Annotation', annotate_image)
                    break

            # Close the window after 'q' is pressed
            cv2.destroyWindow('Image Annotation')

    # Save the annotations to a .txt file
    with open(output_file, 'w') as f:
        for annotation in annotations:
            f.write(annotation + "\n")

    print(f"Annotations saved to {output_file}")

if __name__ == "__main__":
    input_folder = "/home/rguktrkvalley/Music/Buf_cow_cascade/p2"  # Replace with the path to your input image folder
    output_txt_file = "/home/rguktrkvalley/Music/Buf_cow_cascade/p2annotation.txt"  # Replace with the desired output .txt file name

    annotate_images(input_folder, output_txt_file)


'''
import cv2
import os

def annotate_images(folder_path, output_file):
    annotations = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp','.JPEG','.JPG')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Bounding box as the entire image dimensions
            bbox = (0, 0, image.shape[1], image.shape[0])

            # Add the annotation to the list
            annotation = f"{image_path} 1 {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}"
            annotations.append(annotation)

    # Save the annotations to a .txt file
    with open(output_file, 'w') as f:
        for annotation in annotations:
            f.write(annotation + "\n")

    print(f"Annotations saved to {output_file}")

if __name__ == "__main__":
    input_folder = "/home/rguktrkvalley/Music/Buf_cow_cascade/p2"  # Replace with the path to your input image folder
    output_txt_file = "/home/rguktrkvalley/Music/Buf_cow_cascade/p2annotation.txt"  # Replace with the desired output .txt file name

    annotate_images(input_folder, output_txt_file)
'''



