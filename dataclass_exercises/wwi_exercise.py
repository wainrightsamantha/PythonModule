# part i
# create data classes for orders, invoices, customers
from dataclasses import dataclass, field
from datetime import date

@dataclass
class orders:
    id: int
    salesperson_id: int
    invoice_id: int
    order_date: datetime
    recipiant_name: str
    description: str
# part ii
# overide operators > and >=
    def __gt__(self, other):
        return self.order_date > other.order_date
    
    def __ge__(self, other):
        return self.order_date >= other.order_date


@dataclass
class invoices:
    id: int
    description: str
    transaction_amt: float = field(metadata={"units":"dollars"})
    quantity: int
    unit_price: float = field(metadata={"units":"dollars"})
    tax_rate: float = field(metadata={"units":"dollars"})
# part ii 
# overide operators > and >=
    def __gt__(self, other):
        return self.unit_price > other.unit_price
    
    def __ge__(self, other):
        return self.unit_price >= other.unit_price
    
    def __gt__(self, other):
        return self.tax_rate > other.tax_rate
    
    def __ge__(self, other):
        return self.tax_rate >= other.tax_rate

    def __gt__(self, other):
        return self.transaction_amt > other.transaction_amt
    
    def __ge__(self, other):
        return self.transaction_amt >= other.transaction_amt

@dataclass
class customers:
    id: int
    cust_name: str
    phone_num: int
    cust_category: str
    acct_open_date: datetime
    address: str
    zip_code: int
    url: str
    outstanding_bal: bool = field(init=False)

