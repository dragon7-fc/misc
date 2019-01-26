#include <iostream>
#include "cost.h"

using namespace std;

// EXAMPLE OUTPUT:
// Costs for (intended_lane, final_lane, goal_distance):
// ----------------------------------------------------------
// The cost is 0.981684 for (2, 2, 1.0)
// The cost is 0.32968 for (2, 2, 10.0)
// The cost is 0.0392106 for (2, 2, 100.0)
// The cost is 0.0295545 for (1, 2, 100.0)
// The cost is 0.0198013 for (1, 1, 100.0)
// The cost is 0.00995016 for (0, 1, 100.0)
// The cost is 0 for (0, 0, 100.0)
int main() {
    int goal_lane = 0;
    
    //Test cases used for grading - do not change.
    float cost;
    cout << "Costs for (intended_lane, final_lane, goal_distance):" << endl;
    cout << "----------------------------------------------------------" << endl;
    cost = goal_distance_cost(goal_lane, 2, 2, 1.0);
    cout << "The cost is " << cost << " for " << "(2, 2, 1.0)" << endl;
    cost = goal_distance_cost(goal_lane, 2, 2, 10.0);
    cout << "The cost is " << cost << " for " << "(2, 2, 10.0)" << endl;
    cost = goal_distance_cost(goal_lane, 2, 2, 100.0);
    cout << "The cost is " << cost << " for " << "(2, 2, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 1, 2, 100.0);
    cout << "The cost is " << cost << " for " << "(1, 2, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 1, 1, 100.0);
    cout << "The cost is " << cost << " for " << "(1, 1, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 0, 1, 100.0);
    cout << "The cost is " << cost << " for " << "(0, 1, 100.0)" << endl;
    cost = goal_distance_cost(goal_lane, 0, 0, 100.0);
    cout << "The cost is " << cost << " for " << "(0, 0, 100.0)" << endl;
    
    return 0;
}