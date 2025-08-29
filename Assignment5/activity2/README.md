Polymorphism Challenge – Vehicles and Animals 🎭
Overview

This project demonstrates polymorphism in Python. Polymorphism allows objects of different classes to respond to the same method call in different ways. In this program, the move() method behaves differently depending on the object calling it.

Project Description

Base Class: Bicycle

Defines the move() method to describe actions related to bicycles.

Subclasses:

Plane → Overrides move() to describe flying.

Animals → Overrides move() to describe movement based on legs.

Polymorphic Behavior:

Each subclass defines the same method (move()), but with different behavior.

Objects of each class can be called interchangeably while producing unique outputs.

Usage

Instantiate objects from the subclasses:

flying = Plane()
wheels = Bicycle()

Call the move() method with a relevant action:

flying.move("fly")
wheels.move("brake")

Each object responds according to its class implementation.

Expected Output
Aeroplane can fly.
A bicycle can brake.

Key Learning Points

Polymorphism: Same method (move()) behaves differently for different objects.

Method Overriding: Subclasses redefine the parent method to implement their own logic.

Inheritance: Subclasses inherit from the Bicycle base class.

Notes

This project is intended as a mini polymorphism exercise.

It can be extended by adding more vehicles or animals with unique movements.
