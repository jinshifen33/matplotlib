Supporting for drawing Sunburst and Donut charts
-----------------------------------------------------

Donut chart drawing

.. code-block:: python
    import matplotlib.pyplot as plt

    labels = ["Python", "C++", "Ruby", "Java"]
    sizes = [10,30,40,20]
    colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]


    plt.doughnut(sizes, colors=colors, labels=labels, width=0.3,centerlabel="Hello World")
    plt.axis('equal')
    plt.show()

Sunburst chart drawing

.. code-block:: python
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    data = [(180,
        [(50,[10,30,40,20]),(70,[10,30,40,20])
        ,(10,[10,30,40,20]),(50,[10,30,40,20])]
      ),(90,
        [(20,[10,30,40,20]),(70,[10,30,40,20])
        ,(50,[10,30,40,20]),(80,[10,30,40,20])]
      ),(90,
        [(20,[10,30,40,20]),(70,[10,30,40,20])
        ,(50,[10,30,40,20]),(80,[10,30,40,20])]
      )
      ]

    plt.sunburst(data, coloropt=0.8, explode=0.2,centerlabel="hello")
    ax.autoscale()
    plt.show()


    