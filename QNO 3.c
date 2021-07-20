class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size()==0)
            return 0;
        int i=0,j=0;
        int n =s.size();
        int a=1;
        vector<int>v(300,0);
        v[s[0]]++;
        while(j!=n-1)
        {
            if(v[s[j+1]]==0)
            {
                v[s[j+1]]=1;
                j++;
                a=max(a,j-i+1);
            }
            else
            {
                v[s[i]]--;
                i++;
            }
        }
        return a;
}
};
