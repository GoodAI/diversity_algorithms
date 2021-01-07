The command that I used to run the experiment:

```
python3 gym_novelty.py -p 50 -a NS+Fit -e SpaceEngineers-Maze -v all
```

I computed approximately 90 generations before stopping the process.

Definition of the environment:

```python
registered_environments["SpaceEngineers-Maze"] = {
	"bd_func": space_engineers_behavior_descriptor,
	"eval": gym_env.EvaluationFunctor,
	"eval_params": {
		"gym_env_name":"SpaceEngineers-v0",
		"gym_params":{},
		"max_step": 1500,
		"output":"final_reward"},
	"grid_features": {
		"min_x": [-100, -100],
		"max_x": [100, 100],
		"nb_bin": 25
	}
}
```

The reward that is returned by the environment is equal to the final distance of the agent from its starting position.

Behaviour descriptor:

```python
def space_engineers_behavior_descriptor(traj):
  """
  Computes the behavior descriptor from a trajectory.
  Returns the position of the agent in the last observation.
  """
  last_step_data = traj[-1]
  return last_step_data[3]['position']
```

After running the experiment, I exported the resulting behaviour descriptor to show them in the video.
