
def main():
    print("WELCOME TO THE TRIANGLE PRIMITER PROGRAM \nEnter the coordinates of the verticles of a traingle")
    print("VERTEX A")
    vertex_A_x = float(input("Enter X coordinate for vertex A:"))
    vertex_A_y = float(input("Enter Y coordinate for vertex A:"))
    print("VERTEX B")
    vertex_B_x = float(input("Enter X coordinate for vertex B:"))
    vertex_B_y = float(input("Enter Y coordinate for vertex B:"))
    print("VERTEX C")
    vertex_C_x = float(input("Enter X coordinate for vertex C:"))
    vertex_C_y = float(input("Enter Y coordinate for vertex C:"))

    print("SIDE LENGTHS")
    edge_1 = dist(vertex_A_x, vertex_A_y, vertex_B_x, vertex_B_y)
    print("AB = " + edge_1)
    edge_2 = dist(vertex_B_x, vertex_B_y, vertex_C_x, vertex_C_y)
    print("BC = " + edge_2)
    edge_3 = dist(vertex_A_x, vertex_A_y, vertex_C_x, vertex_C_y)
    print("AC = " + edge_3)

    edge_total = str(edge_1 + edge_2 + edge_3)

    print("The permeter of this traingle is" + edge_total)


def dist(x1, y1, x2, y2):
    x_distance = x1 - x2
    y_distance = y1 - y2
    distance_between = float((( x_distance ** 2 ) + ( y_distance ** 2 )) ** 0.5)
    return distance_between

main()