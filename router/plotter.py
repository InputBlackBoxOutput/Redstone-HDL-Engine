import cv2
import numpy as np
from itertools import combinations

class Plotter:
    def __init__(self):
        self.diagram = None

        self.color_red = (0, 0, 255)
        self.color_black = (0, 0, 0)
        self.color_blue = (255, 0, 0)

        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def setup_canvas(self, n_pins_A, n_pins_B, n_tracks):
        width = max(n_pins_A, n_pins_B) * 38
        height = (n_tracks + 2 ) * 25

        self.diagram = np.ones((height, width, 3), np.uint8) * 255

    def add_padding(self):
        top = int(0.4 * self.diagram.shape[0])  # shape[0] = rows
        bottom = top
        left = int(0.4 * self.diagram.shape[1])  # shape[1] = cols
        right = left

        self.diagram = cv2.copyMakeBorder(self.diagram, top, bottom, left, right, cv2.BORDER_CONSTANT, None, (255, 255, 255))

    def draw(self, pins_A, pins_B, tracks):
        self.setup_canvas(len(pins_A), len(pins_B), len(tracks))

        spacing = 40
        n_tracks = len(tracks)

        for i, pin in enumerate(pins_A):
            cv2.putText(self.diagram, pin, (0 + i * spacing, 15), self.font, 0.5, self.color_blue, 1)
        for i, pin in enumerate(pins_B):
            cv2.putText(self.diagram, pin, (0 + i * spacing, 22 * (n_tracks + 2)), self.font, 0.5, self.color_blue, 1)

        for track in tracks:
            for j in tracks[track]:
                h_points = []
                v_points = []
                for i, pin in enumerate(pins_A):
                    if pin == j:
                        x = i * spacing + 5
                        y = track * spacing//2 + 35
                        h_points.append((x, y))
                        v_points.append([(x, 20),(x, y)])

                for i, pin in enumerate(pins_B):
                    if pin == j:
                        x = i * spacing + 5
                        y = track * spacing//2 + 35
                        h_points.append((x, y))

                        _y = (20 * (n_tracks + 2)) - 10
                        v_points.append([(x, _y),(x, y)])

                for line_points in combinations(h_points, 2):
                    cv2.line(self.diagram, line_points[1], line_points[0], self.color_red, 1)

                for line_points in v_points:
                    cv2.line(self.diagram, line_points[1], line_points[0], self.color_black, 1)

        self.add_padding()

    def show(self):
        cv2.imshow("Output", self.diagram)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

if __name__ == "__main__":
    router_output = (['N1', '0', 'N2', 'N3'], ['N3', 'N2', 'N1', '0'], {0: ['N2'], 1: ['N1'], 2: ['N3']})
    
    p = Plotter()
    p.draw(router_output[0], router_output[1], router_output[2])
    p.show()