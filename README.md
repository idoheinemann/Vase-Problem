# Vase Problem

The vase problem is a problem I invented in game theory which is similar to the Prisoner's Dilemma

This code presents a simple API to run Vase Problem games with different virtual agents

## Rules
The problem goes as follows:

Three salesman are trying to sell the same vase

at the first day a buyer comes and offers 5$ for the vase

with each passing day the buyer comes and offers 5$ more than the day before

at each passing day the salesman can either agree to the buyer's deal or disagree to it

the salesman do not know whether their fellow salesman agreed or not until the end of the day

the game ends when one or more salesman agrees to the deal

if only one salesman agreed to the deal, he gets all the money

if two salesman agreed to the deal, each of them gets a quarter of the money, and the one who didn't agree gets half

if all three salesman agreed, each of them gets a third of the money.

the goal of each salesman is to maximise his profit over this repeating scenarios.