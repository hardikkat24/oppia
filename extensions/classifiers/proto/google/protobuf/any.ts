import * as pb_1 from "google-protobuf";
export namespace google.protobuf {
    export class Any extends pb_1.Message {
        constructor(data?: any[] | {
            type_url?: string;
            value?: Uint8Array;
        }) {
            super();
            pb_1.Message.initialize(this, Array.isArray(data) && data, 0, -1, [], null);
            if (!Array.isArray(data) && typeof data == "object") {
                this.type_url = data.type_url;
                this.value = data.value;
            }
        }
        get type_url(): string {
            return pb_1.Message.getFieldWithDefault(this, 1, undefined) as string;
        }
        set type_url(value: string) {
            pb_1.Message.setField(this, 1, value);
        }
        get value(): Uint8Array {
            return pb_1.Message.getFieldWithDefault(this, 2, undefined) as Uint8Array;
        }
        set value(value: Uint8Array) {
            pb_1.Message.setField(this, 2, value);
        }
        toObject() {
            return {
                type_url: this.type_url,
                value: this.value
            };
        }
        serialize(w?: pb_1.BinaryWriter): Uint8Array | undefined {
            const writer = w || new pb_1.BinaryWriter();
            if (typeof this.type_url === "string" && this.type_url.length)
                writer.writeString(1, this.type_url);
            if (this.value !== undefined)
                writer.writeBytes(2, this.value);
            if (!w)
                return writer.getResultBuffer();
        }
        serializeBinary(): Uint8Array { throw new Error("Method not implemented."); }
        static deserialize(bytes: Uint8Array | pb_1.BinaryReader): Any {
            const reader = bytes instanceof Uint8Array ? new pb_1.BinaryReader(bytes) : bytes, message = new Any();
            while (reader.nextField()) {
                if (reader.isEndGroup())
                    break;
                switch (reader.getFieldNumber()) {
                    case 1:
                        message.type_url = reader.readString();
                        break;
                    case 2:
                        message.value = reader.readBytes();
                        break;
                    default: reader.skipField();
                }
            }
            return message;
        }
    }
}
