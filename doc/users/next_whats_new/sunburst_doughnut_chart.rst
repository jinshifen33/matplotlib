Supporting for drawing Sunburst and Donut charts
-----------------------------------------------------

Donut chart drawing
.. code-block:: python
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    data = [30,40,50,60]

    plt.doughnut(data, centerlabel="hello")
    ax.autoscale()
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


    