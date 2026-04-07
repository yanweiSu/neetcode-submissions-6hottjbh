using namespace std;

class Solution {
public:

    string encode(vector<string>& strs) {
        string ret = "";
        for (const string& s : strs) {
            ret += to_string(s.size()) + "#" + s;
        }

        return ret;
    }

    vector<string> decode(string s) {
        int i = 0;
        vector<string> ret;
        string lenstr = "";

        while (i < s.size()) {
            if (s[i] == '#') {
                int strlen = stoi(lenstr);
                ret.push_back(s.substr(i + 1, strlen));
                i = i + strlen + 1;
                lenstr = "";
            } else {
                lenstr += s[i];
                i++;
            }
        }

        return ret;
    }
};
