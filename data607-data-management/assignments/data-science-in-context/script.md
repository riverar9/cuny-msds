# Slides

## Slide 1

1. Hi Everyone! I'm Richie and I will be going over my data science in context presentation. For this presentation I would like to introduce you all to Mage, a tool that I've been playing around with for some time.

## Slide 2

1. As we've seen in this class, there's no Data science without data. So, it is pretty intuitive that we need infrastrucure or plumbing to get our data where it can be used.

2. Mage provides a framework to do just that. Being open source allows for it to be transparent and have quick iterations adding more funcitonality often.

3. It supports a wide array of ways to work with data. It natively has a way to connect to all of the major cloud architectures as well as a wide array of online, local, and unstructured data sources through both batch and streaming.

4. It uses something called Coding Blocks which are it's bread and butter. Using coding blocks allows data engineers and scientists to see every step along the data pipeline and understand what is happening to the data. Additionally, there are visualizations layers built into each block which allows users to analyze the data intuitively as it's being processed.

5. It also have the native ability to enforce data contracts. These are rules that can be shared typically in an XML or JSON file from data source providers which outline key attributes of the data. Think the number of rows, columns, datatypes, any averages and totals, etc. This helps data engineers immediately diagnose issues.

6. Now on the right, there's a gif that's been moving like crazy. This gif is an example of how easy it is. It may move too fast ot see, but you can see that with only 3 clicks a new block was created. Specifically, this block will write to an S3 bucket.

7. The last point I will make is that it allows users to easily either start with blocks or code. Although this seems trivial, this is very powerful as most tools are either only blocks, which inheriently is rigid and difficult to work with, or just code which is verbose and makes the simplist of tasks fairly time consuming. Having the ease of starting with a block and then immediately moving to code allows us to work with the data at the level of sophistication required. Nothing more and nothing less.

Any questions?

## Slide 3

Finally, we're at teh Data pipeline management.

One of the most powerful things about mage is not building a single pipeline but some of the helpful tools built around managing these pipelines. According to their website, their platform can enable data engineers to "Run, monitor, and orchestrate thousands of pipelines without losing sleep.".

I'm not sure if they've had very picky customers who don't have great communication skills, but it's a promising future that they're selling.

1. One of the most useful tools is their alerting system. They have integrations with what any organization would use for the most part. From what I've personally seen, they happily accept new users contributing to their project to add more integrations.

2. These alerts can be on many different types of events. Obviously, any failure or error could become an alert but it can be set on the completion of a pipeline, the successful load of a dataset, or when a series of pipelines complete their run. These are valuable as they can be triggers for AI/ML pipelines downstream.

3. The application keeps logs of all pipelines and events, allowing you to easily pick up where you left off.

4. There are also pipeline triggers native as well. These triggers can be based on a date and a time, or whenever the temperature is under 10 degress farenheit, or on command through an API that you can set up .

5. Lastly, this is portable. This has inherient docker compatibility and can be easily installed onto a docker image for use and reuse.

6. The most common infrastructure I find is that this will be installed on a web hosted VM and managed by an individual. Once installed, teams of engineers and data scientists would connect to that website and work from there. This is powerful as it implicitly enables reproducability and mitigates issues of the "it ran on my computer".

# Demo

Now I have a demo Queued up:

Data url:
    https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

    tests
    print(len(output.columns))
    assert len(output.columns) == 12

Code for rename:

    column_rename_map = {
        'PassengerId'   : 'passenger_id'
        , 'Pclass'      : 'passenger_class'
        , 'Sibsp'       : 'num_siblings_or_spouses_aboard'
        , 'Parch'       : 'num_parents_or_children_aboard'
        , 'Fare'        : 'fare_dollars'
        , 'Embarked'    : 'port_of_embarkation'
        
    }

    data = data.rename(
        columns = column_rename_map
    )
    
    data.columns = map(
        str.lower
        , data.columns
    )

    return data

Data exporter > Local file > "titanic_tickets.csv"

- Looking at the tree, we can see all of our blocks
- This is powerfull as our projects and data landscape becomes more and more complex, we have a graphical way to see what's going on.
- This is even further made easier to manage as these blocks are contained in a pipeline object
- We can use this pipeline object to schedule and more easily orchestrate many pipelines.


There is so much more to this that I couldn't cover, but this tool can be useful to anyone who needs to extract, load, transform, and/or model data.

Thank you for your time!