#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <limits>
#include <numeric>
#include <regex>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <chrono>
#include <queue>

using namespace std;

struct Ally
{
    int y, x, p, id;
};

int N, P, A, X;
int YS, XS;
int myY, myX;
int M;

vector<Ally> allies;
vector<vector<int>> carte;

int minDist(int y1, int x1, int y2, int x2)
{
    if(x1 == x2 && y1 == y2)
        return 0;

    vector<vector<int>> minDist(N, vector<int>(N, 1000000));
    minDist[y1][x1] = 0;
    deque<pair<int, int>> todo(1, make_pair(y1, x1));
    while(!todo.empty())
    {
        auto p = todo.front();
        todo.pop_front();
        int dx[4] = {0, 0, -1, 1};
        int dy[4] = {1, -1, 0, 0};
        int d = minDist[p.first][p.second] + 1;
        for(int i = 0; i < 4; ++i)
        {
            int y = p.first + dy[i];
            int x = p.second + dx[i];
            if(y >= 0 && y < N && x >= 0 && x < N && carte[y][x] == 0 && d < minDist[y][x])
            {
                if(y == y2 && x == x2)
                    return d;

                if(y != YS || x != XS)
                {
                    minDist[y][x] = d;
                    todo.emplace_back(y, x);
                }
            }
        }
    }
    return 1000000;
}

int getY(int i)
{
    if(i < A)
        return allies[i].y;
    if(i == A)
        return myY;
    return YS;
}

int getX(int i)
{
    if(i < A)
        return allies[i].x;
    if(i == A)
        return myX;
    return XS;
}

int solve(const vector<vector<int>>& costMat, int i, int used, int curP)
{
    static map<pair<int, int>, int> mem;
    auto key = make_pair(i, used);
    auto it = mem.lower_bound(key);
    if(it != mem.end() && it->first == key)
        return it->second;

    if(i < A)
    {
        used |= 1 << i;
        curP += allies[i].p;
    }
    int res = curP - costMat[i][M - 1];
    for(int j = 0; j < A; ++j)
    {
        if((used & (1 << j)) == 0)
            res = max(res, solve(costMat, j, used, curP) - costMat[i][j]);
    }

    mem.emplace_hint(it, key, res);
    return res;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> P >> A >> X;
    cin.ignore();

    cin >> myY >> myX;
    cin.ignore();
    --myX;
    --myY;

    cin >> YS >> XS;
    cin.ignore();
    --YS;
    --XS;

    allies.resize(A);
    for(int i = 0; i < A; ++i)
    {
        auto& a = allies[i];
        cin >> a.y >> a.x >> a.p;
        cin.ignore();
        --a.x;
        --a.y;
        a.id = i;
    }

    carte.resize(N);
    for(auto& l : carte)
    {
        l.resize(N);
        for(int& v : l)
        {
            cin >> v;
            cin.ignore();
        }
    }

    M = A + 2;
    vector<vector<int>> costMat(M, vector<int>(M, 1000000));
    for(int i = 0; i < M; ++i)
    {
        costMat[i][i] = 0;
        for(int j = i + 1; j < M; ++j)
        {
            int d = minDist(getY(i), getX(i), getY(j), getX(j));
            costMat[i][j] = d;
            costMat[j][i] = d;
        }
    }

    int ans = solve(costMat, A, 0, P);
    cout << ans << endl;
    if(ans > X)
        cout << "VICTOIRE" << endl;
    else
        cout << "DEFAITE" << endl;

    return 0;
}