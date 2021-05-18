#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include "time_cost.h"

using namespace std;


//add feature: read in factor and builders from .txt
int main(int argc, char *argv[]){
    string fname = argv[1];
    int builders = atoi(argv[2]);
    double factor = atof(argv[3]);
    int th = atoi(argv[4]);
    th -= 12;
    const string TH[3] = {"th12.txt", "th13.txt", "th14.txt"};
    getvals(fname, TH[th], builders, factor);
}

void getvals(string fname, string th, int builders, double factor){
    /*----READ IN VALUES FROM INPUT----*/
    //vector to store the values of lvl, amt, and ug for each line
    vector<UgLine> all_values = read_input_file(fname);

    /*----READ IN NEEDED VALUES FROM ORIGINALCOSTTIME----*/

    //strings to store data from lines in originalcottime.txt
    string lvl_str;
    string ug_str;
    string cost_str;
    string time_str;

    //single line time/cost data converted
    double hours;
    int cost;

    //helper vars for knowing which cumulatives to add to
    //2 characters, tag is b/l/p(builder/lab/pet), type is g/e/d(gold/elix/dark)
    char type;
    char tag;

    //final cumulative times as doubles
    long double totaltime_h = 0, totallab_h = 0, totalpets_h = 0;
    //cumulatives as ints
    long long int totalg = 0, totale = 0, totald = 0;
    long long int totaltime_hi = 0, totaltime_di = 0;
    long long int totallab_hi = 0, totallab_di = 0;
    long long int totalpets_hi = 0, totalpets_di = 0;

    string line;
    
    //loop through each of input line
    for(unsigned int i = 0; i < all_values.size(); i++){
        tag = 'B'; 
        ifstream file(th);

        //loop through original cost/times to find needed lines
        while(getline(file, line)){
            //if not a data line(does not have csv)
            if(line.find(',') == string::npos){
                //check if type change
                if(line.find("Gold") != string::npos){
                    type = 'G';
                }
                else if(line.find("Elixir") != string::npos){
                    type = 'E';
                }
                if(line.find("Dark Elixir") != string::npos){
                    type = 'D';
                }

                //if its a lab line
                if(line.find("Laboratory") != string::npos){
                    tag = 'L';
                }
                //if its a pet line
                if(line.find("Pets") != string::npos){
                    tag = 'P';
                }
                continue;
            }

            //get data into separate strings
            stringstream iss(line);
            getline(iss, lvl_str, ',');
            getline(iss, cost_str, ',');
            getline(iss, time_str, ',');
            getline(iss, ug_str, ',');

            // determine if line is needed, if so place data into correct vectors
            // need ug name to be the same and level to be > the inputs level
            if(ug_str == all_values[i].ug && stoi(lvl_str) > all_values[i].lvl){
                //check if time or cost != N/A, or time != seconds/minutes (skip these cases)
                if(time_str != "N/A" || time_str.find('s') != string::npos || time_str.find('m') != string::npos){
                    //reduce time
                    hours = reduce_time_str(time_str, factor);

                    // multiply by the quantity of the upgrade(Ex. *4 for 4 cannons)
                    hours *= all_values[i].amt;
                }
                if(cost_str != "N/A"){
                    cost = reduce_cost(stoi(cost_str), factor);
                    cost *= all_values[i].amt;
                }
                

                //determine cumulator based on type and lab settings
                if(tag == 'B'){
                    if(type == 'G'){
                        totaltime_h += hours;
                        totalg += cost;
                    }
                    else if(type == 'E'){
                        totaltime_h += hours;
                        totale += cost;
                    }
                    else{
                        totaltime_h += hours;
                        totald += cost;
                    }
                }
                else if(tag == 'L'){
                    if(type == 'E'){
                        totallab_h += hours;
                        totale += cost;
                    }
                    else{
                        totallab_h += hours;
                        totald += cost;
                    }
                }
                else if(tag == 'P'){
                    totalpets_h += hours;
                    totald += cost;
                }
            }
        }
        file.close();
    }
    


    // divide by num builders
    totaltime_h /= builders;

    // convert builder time to ints
    totaltime_hi = round(totaltime_h);
    totaltime_di = totaltime_hi / 24;
    totaltime_hi = totaltime_hi % 24;

    // convert lab time to ints
    totallab_hi = round(totallab_h);
    totallab_di = totallab_hi / 24;
    totallab_hi = totallab_hi % 24;      

    //conver pet time to ints    
    totalpets_hi = round(totalpets_h);
    totalpets_di = totalpets_hi / 24;
    totalpets_hi = totalpets_hi % 24;  

    cout << "Total Time: " << totaltime_di << 'd' << totaltime_hi << 'h' << endl;
    cout << "Total Lab Time: " << totallab_di << 'd' << totallab_hi << 'h' << endl;
    cout << "Total Pet Time: " << totalpets_di << 'd' << totalpets_hi << 'h' << endl;
    cout << "Total Cost: " << endl;
    cout << totalg << " Gold " << endl;
    cout << totale << " Elixir " << endl;
    cout << totald << " Dark " << endl;
}

string time_int_to_string(int days, int hours){
    //convert integer days and hours to string form '_d_h'
    string days_hours;

    days_hours.append(to_string(days));
    days_hours.push_back('d');
    days_hours.append(to_string(hours));
    days_hours.push_back('h');

    return days_hours;
}

double reduce_time(double days, double hours, double factor){
    //make time only hours, subtract factor%, and return
    double reduced_hours;

    //convert to hours and reduce
    hours += days * 24;
    reduced_hours = hours - (hours * factor);

    return reduced_hours;
}

pair<double, double> time_str_to_double(string otime){
    //break time/cost into doubles
    double days, hours;
    string str_days;
    size_t found;

    found = otime.find('d');
    str_days = otime.substr(0, found);
    days = stod(str_days);

    if(otime.find('h') != string::npos){ //if original string time contains an 'h'
        otime.erase(0, found + 1); //erase from begining of string to after the 'd'
        hours = stod(otime); //takes only the num from the hours part of the str
    }
    else{
        hours = 0;
    }

    return make_pair(days, hours);
}

double reduce_time_str(string otime, double factor){
    //break time/cost into doubles, reduce by factor and return
    double days, hours;

    //get string to ints
    pair<double, double> days_hours(time_str_to_double(otime));
    days = days_hours.first; //break apart
    hours = days_hours.second;

    //reduce the time
    hours = reduce_time(days, hours, factor); 

    return hours;
}

int reduce_cost(int o_cost, double factor){
    double final_cost;
    final_cost = o_cost - (o_cost * factor);
    return final_cost;
}

vector<UgLine> read_input_file(string fname){
    /*----READ IN VALUES FROM INPUT----*/
    
    ifstream infile(fname);
    //store variables into UgLine object
    InUgLine singleLine;
    //vector of InUgLines for all the lines to be stored in the input file form
    vector<UgLine> inputValues;

    string line;

    while(getline(infile, line)){
        //get data into separate strings
        stringstream row(line);
        getline(row, singleLine.lvl_str, ',');
        getline(row, singleLine.amt_str, ',');
        getline(row, singleLine.ug_str, ',');
        
        //create a UG_line with correct types
        singleLine.amt_str = singleLine.amt_str.erase(0,1); //remove the 'x' from amount
        UgLine convertedLine{ singleLine.ug_str, stoi(singleLine.lvl_str), stoi(singleLine.amt_str) };
        //push into inputValues vector
        inputValues.push_back(convertedLine);
    }
    infile.close();

    return inputValues;
}



