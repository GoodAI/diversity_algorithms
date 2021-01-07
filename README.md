# Diversity algorithms

This fork contains changes to make it possible to communicate with the Space Engineers game.

## Changes

- Changed log file names so that they are valid on Windows
- Slightly changed the NS+Fit option handling because I was getting some errors with the shape of the fitness. There is probably a better solution.
- Added a Space Engineers maze environment.
- Added a file to export behaviour descriptors to a text file so that they can be rendered in the game.

## How to install

- Install diversity_algorithms (instructions [here](https://github.com/robotsthatdream/diversity_algorithms))
- Install Space Engineers gym (instructions [here](https://github.com/GoodAI/SpaceEngineersGym))

*Notes:*
Scoop is not working with the Space Engineers gym.

## How to use

`SpaceEngineers-Maze` environment was added to the dictionary of registered environments. The description of the environment can be found [here](https://github.com/GoodAI/SpaceEngineersGym).

After running an experiment, it is possible to export behaviour descriptors to a text file and later use them with the [*/BDs load \<filename\>*](https://github.com/GoodAI/iv4xr-se-plugin#bds-load-filename) command. In order to do that, run the *diversity_algorithms/space_engineers/export_behaviours.py* like this:

```
python3 export_behaviours.py folder_with_results output.txt
```
