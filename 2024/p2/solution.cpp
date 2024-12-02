#include <iostream>
#include <fstream>
#include <sstream>

std::ifstream input("input.txt");

std::vector<std::vector<int>> read_input()
{
  std::vector<std::vector<int>> result;
  std::string line;

  while (std::getline(input, line))
  {
    std::vector<int> row;
    std::istringstream iss(line);
    int num;

    while (iss >> num)
    {
      row.push_back(num);
    }

    result.push_back(row);
  }

  return result;
}

int abs(int a, int b)
{
  return a > b ? a - b : b - a;
}

bool check_report_safety(std::vector<int> report, bool asc)
{
  for (size_t j = 0; j < report.size() - 1; j++)
  {
    bool cont = asc ? report[j] < report[j + 1] : report[j] > report[j + 1];
    if (!cont)
    {
      return false;
    }

    int diff = abs(report[j], report[j + 1]);
    if (diff > 3)
    {
      return false;
    }
  }

  return true;
}

int part1(std::vector<std::vector<int>> input)
{

  int num_reports_safe = 0;

  for (size_t i = 0; i < input.size(); i++)
  {

    bool asc = input[i][0] < input[i][1];
    check_report_safety(input[i], asc) && num_reports_safe++;
  }

  return num_reports_safe;
}

int part2(std::vector<std::vector<int>> input)
{

  int num_reports_safe = 0;
  for (size_t i = 0; i < input.size(); i++)
  {

    bool asc = input[i][0] < input[i][1];
    bool safe = check_report_safety(input[i], asc);
    if (safe)
    {
      num_reports_safe++;
      continue;
    }

    for (size_t j = 0; j < input[i].size(); j++)
    {
      std::vector<int> copy = input[i];
      copy.erase(copy.begin() + j);

      bool asc = copy[0] < copy[1];
      safe = check_report_safety(copy, asc);
      if (safe)
      {
        num_reports_safe++;
        break;
      }
    }
  }

  return num_reports_safe;
}

int main()
{
  std::vector<std::vector<int>> input = read_input();
  std::cout << "p1: num reports safe: " << part1(input) << std::endl;
  std::cout << "p2: num reports safe: " << part2(input) << std::endl;
  return 0;
}
