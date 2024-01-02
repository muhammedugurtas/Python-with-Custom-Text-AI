# Text AI by Poncik 

Hello, I have done this project before, but today I thought why not upload it to githuba and uploaded it to githuba.

The aim of my project was to write an application where people can make a simple command AI by themselves. So I created a very simple version of it in python.

## How to use it?

- First, download the repository
- And start ai.py file **(This is the file where we give commands to our AI)**

## ai.py File Instructions

When we initialize the file we will get an input like this:

```sh
You: 
```

Here it asks us for a command to give to our AI. SUFFIX is defaulted to Poncik. Therefore, when giving our command, we should make sure that it starts with Poncik or poncik. For example:

```sh
You: Poncik turn on lights
```

When we give a command, it will find the command closest to that command from the json file and bring us the result.

```sh
You: Poncik turn on lights
AI: I'm turning on the lights

AI: I got "lights_on" command.
```

'I got "lights_on" command.' In this section we can see what the command name of the response is. This makes it easier when we are doing an automation.


## ai_modification.py File Instructions

When we initialize the file we will get an input like this:

```sh
AI: Are you want add new command? y\Y or n\N: 
```

If we select y(Yes) it will ask us for the command information we want to add.

First, we will get this:

```sh
Command: 
```

Here we enter the command that the user will type.

```sh
Command: Turn off the computer
```

Then, we will get this:

```sh
Answer: 
```

Here we enter the message that the AI will send when the user gives the command.

```sh
Answer: I'm turning off the computer
```

Then, we will get this:

```sh
Command Name: 
```

Here we enter the command name that will be useful when the command is issued.

```sh
Command Name: turn_on_computer
```

Then, we will get this:

```sh
AI: Are you sure? y\\Y or n\\N: 
```

If we enter y(Yes) here, the command will be created successfully.

```sh
AI: New command added successfuly.
```
