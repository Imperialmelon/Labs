from python_lab_oop import abstract, circle, kvadrat, rectangle

def main():
    circle_ = circle.circle(15, 'Синий')
    circle_.repr()
    kvadrat_ = kvadrat.kvadrat(10, 'Желтый')
    kvadrat_.repr()
    rectangle_ = rectangle.rectangle(5, 20, 'Черный')
    rectangle_.repr()

if __name__ == '__main__':
    main()
