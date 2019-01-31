#include <iostream>
#include <vector>
#include "hybrid_breadth_first.h"

using std::cout;
using std::endl;

// Sets up maze grid
int X = 1;
int _ = 0;

/**
 * TODO: You can change up the grid maze to test different expansions.
 */
vector<vector<int>> GRID = {
  {_,X,X,_,_,_,_,_,_,_,X,X,_,_,_,_,},
  {_,X,X,_,_,_,_,_,_,X,X,_,_,_,_,_,},
  {_,X,X,_,_,_,_,_,X,X,_,_,_,_,_,_,},
  {_,X,X,_,_,_,_,X,X,_,_,_,X,X,X,_,},
  {_,X,X,_,_,_,X,X,_,_,_,X,X,X,_,_,},
  {_,X,X,_,_,X,X,_,_,_,X,X,X,_,_,_,},
  {_,X,X,_,X,X,_,_,_,X,X,X,_,_,_,_,},
  {_,X,X,X,X,_,_,_,X,X,X,_,_,_,_,_,},
  {_,X,X,X,_,_,_,X,X,X,_,_,_,_,_,_,},
  {_,X,X,_,_,_,X,X,X,_,_,X,X,X,X,X,},
  {_,X,_,_,_,X,X,X,_,_,X,X,X,X,X,X,},
  {_,_,_,_,X,X,X,_,_,X,X,X,X,X,X,X,},
  {_,_,_,X,X,X,_,_,X,X,X,X,X,X,X,X,},
  {_,_,X,X,X,_,_,X,X,X,X,X,X,X,X,X,},
  {_,X,X,X,_,_,_,_,_,_,_,_,_,_,_,_,},
  {X,X,X,_,_,_,_,_,_,_,_,_,_,_,_,_,}};

vector<double> START = {0.0,0.0,0.0};
vector<int> GOAL = {(int)GRID.size()-1, (int)GRID[0].size()-1};

// EXAMPLE OUTPUT:
// Finding path through grid:
// 0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0
// 0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0
// 0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0
// 0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,0
// 0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0
// 0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0
// 0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0
// 0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0
// 0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0
// 0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1
// 0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1
// 0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1
// 0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1
// 0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1
// 0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0
// 1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0
// found path to goal in 10082 expansions
// show path from start to finish
// ##### step 1 #####
// x 1.45
// y 0
// theta 0
// ##### step 2 #####
// x 2.9
// y 0
// theta 0
// ##### step 3 #####
// x 4.35
// y 0
// theta 0.511348
// ##### step 4 #####
// x 5.61452
// y 0.709563
// theta 6.01748
// ##### step 5 #####
// x 7.01364
// y 0.328808
// theta 6.2712
// ##### step 6 #####
// x 8.46354
// y 0.311427
// theta 6.2712
// ##### step 7 #####
// x 9.91343
// y 0.294046
// theta 6.78255
// ##### step 8 #####
// x 11.1864
// y 0.9884
// theta 7.29389
// ##### step 9 #####
// x 11.9567
// y 2.21685
// theta 8.64619
// ##### step 10 #####
// x 10.9244
// y 3.23515
// theta 8.39247
// ##### step 11 #####
// x 10.1808
// y 4.47996
// theta 8.13875
// ##### step 12 #####
// x 9.77346
// y 5.87156
// theta 8.91581
// ##### step 13 #####
// x 8.50726
// y 6.57812
// theta 8.66209
// ##### step 14 #####
// x 7.45893
// y 7.57988
// theta 8.40837
// ##### step 15 #####
// x 6.69562
// y 8.8127
// theta 9.46388
// ##### step 16 #####
// x 5.24673
// y 8.75601
// theta 8.40837
// ##### step 17 #####
// x 4.48341
// y 9.98883
// theta 8.40837
// ##### step 18 #####
// x 3.7201
// y 11.2217
// theta 8.40837
// ##### step 19 #####
// x 2.95678
// y 12.4545
// theta 8.15465
// ##### step 20 #####
// x 2.52735
// y 13.8394
// theta 7.64331
// ##### step 21 #####
// x 2.83057
// y 15.2574
// theta 5.96899
// ##### step 22 #####
// x 4.20959
// y 14.8092
// theta 6.48034
// ##### step 23 #####
// x 5.6315
// y 15.0933
// theta 5.70329
// ##### step 24 #####
// x 6.84445
// y 14.2988
// theta 5.44957
// ##### step 25 #####
// x 7.81914
// y 13.2252
// theta 5.19585
// ##### step 26 #####
// x 8.49317
// y 11.9414
// theta 5.19585
// ##### step 27 #####
// x 9.1672
// y 10.6576
// theta 5.44957
// ##### step 28 #####
// x 10.1419
// y 9.58405
// theta 5.44957
// ##### step 29 #####
// x 11.1166
// y 8.51052
// theta 5.70329
// ##### step 30 #####
// x 12.3295
// y 7.716
// theta 5.70329
// ##### step 31 #####
// x 13.5425
// y 6.92149
// theta 7.05558
// ##### step 32 #####
// x 14.581
// y 7.93337
// theta 8.11109
// ##### step 33 #####
// x 14.2123
// y 9.33571
// theta 7.59974
// ##### step 34 #####
// x 14.577
// y 10.7391
// theta 7.59974
// ##### step 35 #####
// x 14.9417
// y 12.1425
// theta 7.59974
// ##### step 36 #####
// x 15.3064
// y 13.5459
// theta 8.65526
// ##### step 37 #####
// x 14.2649
// y 14.5548
// theta 7.30296
// ##### step 38 #####
// x 15.0241
// y 15.7902
// theta 9.33357

int main() {
  cout << "Finding path through grid:" << endl;
  
  // Creates an Empty Maze and for testing the number of expansions with it
  for(int i = 0; i < GRID.size(); ++i) {
    cout << GRID[i][0];
    for(int j = 1; j < GRID[0].size(); ++j) {
      cout << "," << GRID[i][j];
    }
    cout << endl;
  }

  HBF hbf = HBF();

  HBF::maze_path get_path = hbf.search(GRID,START,GOAL);

  vector<HBF::maze_s> show_path = hbf.reconstruct_path(get_path.came_from, 
                                                       START, get_path.final);

  cout << "show path from start to finish" << endl;
  for(int i = show_path.size()-1; i >= 0; --i) {
      HBF::maze_s step = show_path[i];
      cout << "##### step " << step.g << " #####" << endl;
      cout << "x " << step.x << endl;
      cout << "y " << step.y << endl;
      cout << "theta " << step.theta << endl;
  }
  
  return 0;
}