# nvperf

## Usage

To use the tool, specify paths for nvprof result files.
The timeline file contains data on top kernels and their % of overall runtime.
The metrics file contains data like 'dp\_flop\_eff' for each kernel.
The tool correlates data from both files to compute overall flop rate.

See example below :

```
$ ./nvperf.py -mf=./inputs/mmf-metricsfile.csv -tf=./inputs/mmf-timelinefile.csv
Namespace(metrics_file='./inputs/mmf-metricsfile.csv', timeline_file='./inputs/mmf-timelinefile.csv')
('Flops (% peak): ', 1.87928511503332)

```
