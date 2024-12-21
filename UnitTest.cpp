#include "Solution.hpp"
#include <iostream>

struct TestCase {
    int n;
    vector<vector<int>> edges;
    vector<int> values;
    int k, output;
};

class UnitTest {
private:
    vector<TestCase> testcases;
    Solution obj;

public:
    UnitTest() {
        testcases = {{5, {{0,2},{1,2},{1,3},{2,4}}, {1,8,1,4,4}, 6, 2},
                     {7, {{0,1},{0,2},{1,3},{1,4},{2,5},{2,6}}, {3,0,6,1,5,2,1}, 3, 3}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            int n = testcases[i].n;
            vector<vector<int>> edges = testcases[i].edges;
            vector<int> values = testcases[i].values;
            int k = testcases[i].k;
            int output = testcases[i].output;


            int result = obj.maxKDivisibleComponents(n, edges, values, k)
            cout << "TestCase " << i+1 << ": " << ((result == output) ? "passed":"failed");
        }
    }
};