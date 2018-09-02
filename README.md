# compare-recordclass
Compare recordclass with namedtuple and dataclass

## Object size

| Module      | Size |
| ----------- | ----:|
| namedtuple  | 96   |
| recordclass | 96   |
| dataclass   | 56   |

`dataclass` wins clearly.

## Time to finish

| Module      | Create | Sum by index | Sum by name | Sort  |
| ----------- | ------:| ------------:| -----------:| -----:|
| namedtuple  | 0.505  | 0.283        | 0.482       | 0.383 |
| recordclass | 0.459  | 0.275        | 0.297       | 0.400 |
| dataclass   | 0.682  | -            | 0.396       | -     |
