// ORM class for table 'train_tickets'
// WARNING: This class is AUTO-GENERATED. Modify at your own risk.
//
// Debug information:
// Generated date: Sat Apr 26 18:26:48 MSK 2025
// For connector: org.apache.sqoop.manager.PostgresqlManager
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapred.lib.db.DBWritable;
import org.apache.sqoop.lib.JdbcWritableBridge;
import org.apache.sqoop.lib.DelimiterSet;
import org.apache.sqoop.lib.FieldFormatter;
import org.apache.sqoop.lib.RecordParser;
import org.apache.sqoop.lib.BooleanParser;
import org.apache.sqoop.lib.BlobRef;
import org.apache.sqoop.lib.ClobRef;
import org.apache.sqoop.lib.LargeObjectLoader;
import org.apache.sqoop.lib.SqoopRecord;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class train_tickets extends SqoopRecord  implements DBWritable, Writable {
  private final int PROTOCOL_VERSION = 3;
  public int getClassFormatVersion() { return PROTOCOL_VERSION; }
  public static interface FieldSetterCommand {    void setField(Object value);  }  protected ResultSet __cur_result_set;
  private Map<String, FieldSetterCommand> setters = new HashMap<String, FieldSetterCommand>();
  private void init0() {
    setters.put("id", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.id = (Integer)value;
      }
    });
    setters.put("origin", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.origin = (String)value;
      }
    });
    setters.put("destination", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.destination = (String)value;
      }
    });
    setters.put("departure", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.departure = (java.sql.Timestamp)value;
      }
    });
    setters.put("arrival", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.arrival = (java.sql.Timestamp)value;
      }
    });
    setters.put("duration", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.duration = (java.math.BigDecimal)value;
      }
    });
    setters.put("vehicle_type", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.vehicle_type = (String)value;
      }
    });
    setters.put("vehicle_class", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.vehicle_class = (String)value;
      }
    });
    setters.put("price", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.price = (java.math.BigDecimal)value;
      }
    });
    setters.put("fare", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        train_tickets.this.fare = (String)value;
      }
    });
  }
  public train_tickets() {
    init0();
  }
  private Integer id;
  public Integer get_id() {
    return id;
  }
  public void set_id(Integer id) {
    this.id = id;
  }
  public train_tickets with_id(Integer id) {
    this.id = id;
    return this;
  }
  private String origin;
  public String get_origin() {
    return origin;
  }
  public void set_origin(String origin) {
    this.origin = origin;
  }
  public train_tickets with_origin(String origin) {
    this.origin = origin;
    return this;
  }
  private String destination;
  public String get_destination() {
    return destination;
  }
  public void set_destination(String destination) {
    this.destination = destination;
  }
  public train_tickets with_destination(String destination) {
    this.destination = destination;
    return this;
  }
  private java.sql.Timestamp departure;
  public java.sql.Timestamp get_departure() {
    return departure;
  }
  public void set_departure(java.sql.Timestamp departure) {
    this.departure = departure;
  }
  public train_tickets with_departure(java.sql.Timestamp departure) {
    this.departure = departure;
    return this;
  }
  private java.sql.Timestamp arrival;
  public java.sql.Timestamp get_arrival() {
    return arrival;
  }
  public void set_arrival(java.sql.Timestamp arrival) {
    this.arrival = arrival;
  }
  public train_tickets with_arrival(java.sql.Timestamp arrival) {
    this.arrival = arrival;
    return this;
  }
  private java.math.BigDecimal duration;
  public java.math.BigDecimal get_duration() {
    return duration;
  }
  public void set_duration(java.math.BigDecimal duration) {
    this.duration = duration;
  }
  public train_tickets with_duration(java.math.BigDecimal duration) {
    this.duration = duration;
    return this;
  }
  private String vehicle_type;
  public String get_vehicle_type() {
    return vehicle_type;
  }
  public void set_vehicle_type(String vehicle_type) {
    this.vehicle_type = vehicle_type;
  }
  public train_tickets with_vehicle_type(String vehicle_type) {
    this.vehicle_type = vehicle_type;
    return this;
  }
  private String vehicle_class;
  public String get_vehicle_class() {
    return vehicle_class;
  }
  public void set_vehicle_class(String vehicle_class) {
    this.vehicle_class = vehicle_class;
  }
  public train_tickets with_vehicle_class(String vehicle_class) {
    this.vehicle_class = vehicle_class;
    return this;
  }
  private java.math.BigDecimal price;
  public java.math.BigDecimal get_price() {
    return price;
  }
  public void set_price(java.math.BigDecimal price) {
    this.price = price;
  }
  public train_tickets with_price(java.math.BigDecimal price) {
    this.price = price;
    return this;
  }
  private String fare;
  public String get_fare() {
    return fare;
  }
  public void set_fare(String fare) {
    this.fare = fare;
  }
  public train_tickets with_fare(String fare) {
    this.fare = fare;
    return this;
  }
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof train_tickets)) {
      return false;
    }
    train_tickets that = (train_tickets) o;
    boolean equal = true;
    equal = equal && (this.id == null ? that.id == null : this.id.equals(that.id));
    equal = equal && (this.origin == null ? that.origin == null : this.origin.equals(that.origin));
    equal = equal && (this.destination == null ? that.destination == null : this.destination.equals(that.destination));
    equal = equal && (this.departure == null ? that.departure == null : this.departure.equals(that.departure));
    equal = equal && (this.arrival == null ? that.arrival == null : this.arrival.equals(that.arrival));
    equal = equal && (this.duration == null ? that.duration == null : this.duration.equals(that.duration));
    equal = equal && (this.vehicle_type == null ? that.vehicle_type == null : this.vehicle_type.equals(that.vehicle_type));
    equal = equal && (this.vehicle_class == null ? that.vehicle_class == null : this.vehicle_class.equals(that.vehicle_class));
    equal = equal && (this.price == null ? that.price == null : this.price.equals(that.price));
    equal = equal && (this.fare == null ? that.fare == null : this.fare.equals(that.fare));
    return equal;
  }
  public boolean equals0(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof train_tickets)) {
      return false;
    }
    train_tickets that = (train_tickets) o;
    boolean equal = true;
    equal = equal && (this.id == null ? that.id == null : this.id.equals(that.id));
    equal = equal && (this.origin == null ? that.origin == null : this.origin.equals(that.origin));
    equal = equal && (this.destination == null ? that.destination == null : this.destination.equals(that.destination));
    equal = equal && (this.departure == null ? that.departure == null : this.departure.equals(that.departure));
    equal = equal && (this.arrival == null ? that.arrival == null : this.arrival.equals(that.arrival));
    equal = equal && (this.duration == null ? that.duration == null : this.duration.equals(that.duration));
    equal = equal && (this.vehicle_type == null ? that.vehicle_type == null : this.vehicle_type.equals(that.vehicle_type));
    equal = equal && (this.vehicle_class == null ? that.vehicle_class == null : this.vehicle_class.equals(that.vehicle_class));
    equal = equal && (this.price == null ? that.price == null : this.price.equals(that.price));
    equal = equal && (this.fare == null ? that.fare == null : this.fare.equals(that.fare));
    return equal;
  }
  public void readFields(ResultSet __dbResults) throws SQLException {
    this.__cur_result_set = __dbResults;
    this.id = JdbcWritableBridge.readInteger(1, __dbResults);
    this.origin = JdbcWritableBridge.readString(2, __dbResults);
    this.destination = JdbcWritableBridge.readString(3, __dbResults);
    this.departure = JdbcWritableBridge.readTimestamp(4, __dbResults);
    this.arrival = JdbcWritableBridge.readTimestamp(5, __dbResults);
    this.duration = JdbcWritableBridge.readBigDecimal(6, __dbResults);
    this.vehicle_type = JdbcWritableBridge.readString(7, __dbResults);
    this.vehicle_class = JdbcWritableBridge.readString(8, __dbResults);
    this.price = JdbcWritableBridge.readBigDecimal(9, __dbResults);
    this.fare = JdbcWritableBridge.readString(10, __dbResults);
  }
  public void readFields0(ResultSet __dbResults) throws SQLException {
    this.id = JdbcWritableBridge.readInteger(1, __dbResults);
    this.origin = JdbcWritableBridge.readString(2, __dbResults);
    this.destination = JdbcWritableBridge.readString(3, __dbResults);
    this.departure = JdbcWritableBridge.readTimestamp(4, __dbResults);
    this.arrival = JdbcWritableBridge.readTimestamp(5, __dbResults);
    this.duration = JdbcWritableBridge.readBigDecimal(6, __dbResults);
    this.vehicle_type = JdbcWritableBridge.readString(7, __dbResults);
    this.vehicle_class = JdbcWritableBridge.readString(8, __dbResults);
    this.price = JdbcWritableBridge.readBigDecimal(9, __dbResults);
    this.fare = JdbcWritableBridge.readString(10, __dbResults);
  }
  public void loadLargeObjects(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void loadLargeObjects0(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void write(PreparedStatement __dbStmt) throws SQLException {
    write(__dbStmt, 0);
  }

  public int write(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeInteger(id, 1 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(origin, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(destination, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeTimestamp(departure, 4 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeTimestamp(arrival, 5 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(duration, 6 + __off, 2, __dbStmt);
    JdbcWritableBridge.writeString(vehicle_type, 7 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(vehicle_class, 8 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(price, 9 + __off, 2, __dbStmt);
    JdbcWritableBridge.writeString(fare, 10 + __off, 12, __dbStmt);
    return 10;
  }
  public void write0(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeInteger(id, 1 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(origin, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(destination, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeTimestamp(departure, 4 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeTimestamp(arrival, 5 + __off, 93, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(duration, 6 + __off, 2, __dbStmt);
    JdbcWritableBridge.writeString(vehicle_type, 7 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(vehicle_class, 8 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(price, 9 + __off, 2, __dbStmt);
    JdbcWritableBridge.writeString(fare, 10 + __off, 12, __dbStmt);
  }
  public void readFields(DataInput __dataIn) throws IOException {
this.readFields0(__dataIn);  }
  public void readFields0(DataInput __dataIn) throws IOException {
    if (__dataIn.readBoolean()) { 
        this.id = null;
    } else {
    this.id = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.origin = null;
    } else {
    this.origin = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.destination = null;
    } else {
    this.destination = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.departure = null;
    } else {
    this.departure = new Timestamp(__dataIn.readLong());
    this.departure.setNanos(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.arrival = null;
    } else {
    this.arrival = new Timestamp(__dataIn.readLong());
    this.arrival.setNanos(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.duration = null;
    } else {
    this.duration = org.apache.sqoop.lib.BigDecimalSerializer.readFields(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.vehicle_type = null;
    } else {
    this.vehicle_type = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.vehicle_class = null;
    } else {
    this.vehicle_class = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.price = null;
    } else {
    this.price = org.apache.sqoop.lib.BigDecimalSerializer.readFields(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.fare = null;
    } else {
    this.fare = Text.readString(__dataIn);
    }
  }
  public void write(DataOutput __dataOut) throws IOException {
    if (null == this.id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.id);
    }
    if (null == this.origin) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, origin);
    }
    if (null == this.destination) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, destination);
    }
    if (null == this.departure) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.departure.getTime());
    __dataOut.writeInt(this.departure.getNanos());
    }
    if (null == this.arrival) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.arrival.getTime());
    __dataOut.writeInt(this.arrival.getNanos());
    }
    if (null == this.duration) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    org.apache.sqoop.lib.BigDecimalSerializer.write(this.duration, __dataOut);
    }
    if (null == this.vehicle_type) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, vehicle_type);
    }
    if (null == this.vehicle_class) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, vehicle_class);
    }
    if (null == this.price) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    org.apache.sqoop.lib.BigDecimalSerializer.write(this.price, __dataOut);
    }
    if (null == this.fare) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, fare);
    }
  }
  public void write0(DataOutput __dataOut) throws IOException {
    if (null == this.id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.id);
    }
    if (null == this.origin) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, origin);
    }
    if (null == this.destination) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, destination);
    }
    if (null == this.departure) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.departure.getTime());
    __dataOut.writeInt(this.departure.getNanos());
    }
    if (null == this.arrival) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.arrival.getTime());
    __dataOut.writeInt(this.arrival.getNanos());
    }
    if (null == this.duration) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    org.apache.sqoop.lib.BigDecimalSerializer.write(this.duration, __dataOut);
    }
    if (null == this.vehicle_type) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, vehicle_type);
    }
    if (null == this.vehicle_class) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, vehicle_class);
    }
    if (null == this.price) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    org.apache.sqoop.lib.BigDecimalSerializer.write(this.price, __dataOut);
    }
    if (null == this.fare) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, fare);
    }
  }
  private static final DelimiterSet __outputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  public String toString() {
    return toString(__outputDelimiters, true);
  }
  public String toString(DelimiterSet delimiters) {
    return toString(delimiters, true);
  }
  public String toString(boolean useRecordDelim) {
    return toString(__outputDelimiters, useRecordDelim);
  }
  public String toString(DelimiterSet delimiters, boolean useRecordDelim) {
    StringBuilder __sb = new StringBuilder();
    char fieldDelim = delimiters.getFieldsTerminatedBy();
    __sb.append(FieldFormatter.escapeAndEnclose(id==null?"null":"" + id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(origin==null?"null":origin, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(destination==null?"null":destination, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(departure==null?"null":"" + departure, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(arrival==null?"null":"" + arrival, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(duration==null?"null":duration.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(vehicle_type==null?"null":vehicle_type, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(vehicle_class==null?"null":vehicle_class, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(price==null?"null":price.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(fare==null?"null":fare, delimiters));
    if (useRecordDelim) {
      __sb.append(delimiters.getLinesTerminatedBy());
    }
    return __sb.toString();
  }
  public void toString0(DelimiterSet delimiters, StringBuilder __sb, char fieldDelim) {
    __sb.append(FieldFormatter.escapeAndEnclose(id==null?"null":"" + id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(origin==null?"null":origin, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(destination==null?"null":destination, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(departure==null?"null":"" + departure, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(arrival==null?"null":"" + arrival, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(duration==null?"null":duration.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(vehicle_type==null?"null":vehicle_type, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(vehicle_class==null?"null":vehicle_class, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(price==null?"null":price.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(fare==null?"null":fare, delimiters));
  }
  private static final DelimiterSet __inputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  private RecordParser __parser;
  public void parse(Text __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharSequence __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(byte [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(char [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(ByteBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  private void __loadFromFields(List<String> fields) {
    Iterator<String> __it = fields.listIterator();
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.id = null; } else {
      this.id = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.origin = null; } else {
      this.origin = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.destination = null; } else {
      this.destination = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.departure = null; } else {
      this.departure = java.sql.Timestamp.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.arrival = null; } else {
      this.arrival = java.sql.Timestamp.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.duration = null; } else {
      this.duration = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.vehicle_type = null; } else {
      this.vehicle_type = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.vehicle_class = null; } else {
      this.vehicle_class = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.price = null; } else {
      this.price = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.fare = null; } else {
      this.fare = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  private void __loadFromFields0(Iterator<String> __it) {
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.id = null; } else {
      this.id = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.origin = null; } else {
      this.origin = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.destination = null; } else {
      this.destination = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.departure = null; } else {
      this.departure = java.sql.Timestamp.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.arrival = null; } else {
      this.arrival = java.sql.Timestamp.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.duration = null; } else {
      this.duration = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.vehicle_type = null; } else {
      this.vehicle_type = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.vehicle_class = null; } else {
      this.vehicle_class = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.price = null; } else {
      this.price = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.fare = null; } else {
      this.fare = __cur_str;
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  public Object clone() throws CloneNotSupportedException {
    train_tickets o = (train_tickets) super.clone();
    o.departure = (o.departure != null) ? (java.sql.Timestamp) o.departure.clone() : null;
    o.arrival = (o.arrival != null) ? (java.sql.Timestamp) o.arrival.clone() : null;
    return o;
  }

  public void clone0(train_tickets o) throws CloneNotSupportedException {
    o.departure = (o.departure != null) ? (java.sql.Timestamp) o.departure.clone() : null;
    o.arrival = (o.arrival != null) ? (java.sql.Timestamp) o.arrival.clone() : null;
  }

  public Map<String, Object> getFieldMap() {
    Map<String, Object> __sqoop$field_map = new HashMap<String, Object>();
    __sqoop$field_map.put("id", this.id);
    __sqoop$field_map.put("origin", this.origin);
    __sqoop$field_map.put("destination", this.destination);
    __sqoop$field_map.put("departure", this.departure);
    __sqoop$field_map.put("arrival", this.arrival);
    __sqoop$field_map.put("duration", this.duration);
    __sqoop$field_map.put("vehicle_type", this.vehicle_type);
    __sqoop$field_map.put("vehicle_class", this.vehicle_class);
    __sqoop$field_map.put("price", this.price);
    __sqoop$field_map.put("fare", this.fare);
    return __sqoop$field_map;
  }

  public void getFieldMap0(Map<String, Object> __sqoop$field_map) {
    __sqoop$field_map.put("id", this.id);
    __sqoop$field_map.put("origin", this.origin);
    __sqoop$field_map.put("destination", this.destination);
    __sqoop$field_map.put("departure", this.departure);
    __sqoop$field_map.put("arrival", this.arrival);
    __sqoop$field_map.put("duration", this.duration);
    __sqoop$field_map.put("vehicle_type", this.vehicle_type);
    __sqoop$field_map.put("vehicle_class", this.vehicle_class);
    __sqoop$field_map.put("price", this.price);
    __sqoop$field_map.put("fare", this.fare);
  }

  public void setField(String __fieldName, Object __fieldVal) {
    if (!setters.containsKey(__fieldName)) {
      throw new RuntimeException("No such field:"+__fieldName);
    }
    setters.get(__fieldName).setField(__fieldVal);
  }

}
