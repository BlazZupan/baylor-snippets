import Orange
import pandas as pd
from os.path import expanduser

m = in_object

names = ["%s-%d" % (str(d.get_class()), int(d["Time"])) for d in m.row_items]
X = Orange.data.Table(m.data).X
frame = pd.DataFrame(X, columns=names, index=names)

writer = pd.ExcelWriter(expanduser("~/Desktop/") + "distances.xlsx")
frame.to_excel(writer, "Distances")
writer.save()