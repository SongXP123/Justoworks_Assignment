import csv


class justworks:
    def __init__(self, file_name) -> None:
        # store the customer amount for each month
        self.dic = {}
        # keep track of the lowest and highest amount for each customer for each month
        self.low = {}
        self.high = {}
        self.file_name = file_name
    
    # Process the data from csv file
    def process_data(self):
        with open(self.file_name) as input_file:
            # if has header row
            # heading = next(file)
            self.reader = csv.reader(input_file)

            for row in self.reader:
                custumor_id = row[0]
                date = row[1]
                amount = row[2]

                # ignore empty row
                if not custumor_id or not date or not amount:
                    continue
                
                # get the month and year of each row
                date = date.split('/')
                month_year = date[0] + '/' + date[2]

                # use (custumor_id, month_year) as key
                if (custumor_id, month_year) not in self.dic:
                    self.dic[(custumor_id, month_year)] = 0
                    self.low[(custumor_id, month_year)] = float("inf")
                    self.high[(custumor_id, month_year)] = float("-inf")
                
                # update the amount
                amount = int(amount)
                self.dic[(custumor_id, month_year)] += amount
                current_amount = self.dic[(custumor_id, month_year)]

                maximum_amount = self.high[(custumor_id, month_year)]
                self.high[(custumor_id, month_year)] = max(current_amount, maximum_amount)
                minimum_amount = self.low[(custumor_id, month_year)]
                self.low[(custumor_id, month_year)] = min(current_amount, minimum_amount)
    
    # Output the final result to a new csv file
    def output(self):
        self.process_data()

        # store the correct row in the data for output
        data = []
        for key in self.dic.keys():
            row = []
            customer_id, month_year = key
            row.append(customer_id)
            row.append(month_year)
            minBalance = self.low[key]
            maxBalance = self.high[key]
            endingBalance = self.dic[key]
            row.append(minBalance)
            row.append(maxBalance)
            row.append(endingBalance)
            data.append(row)

        with open('output.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            heading = ['CustomerID', 'MM/YYYY', 'MinBalance', 'MaxBalance', 'EndingBalance']
            writer.writerow(heading)
            for row in data:
                writer.writerow(row)
        



if __name__ == '__main__':
    demo = justworks('dataset.csv')
    demo.output()
